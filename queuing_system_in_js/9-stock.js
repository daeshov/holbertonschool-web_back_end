const express = require('express');
const redis = require('redis');
const { promisify } = require('util');

const app = express();
const port = 1245;

const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);

const listProducts = [
  { itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4 },
  { itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10 },
  { itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2 },
  { itemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5 },
];

// Function to get an item by its ID
function getItemById(itemId) {
  return listProducts.find((product) => product.itemId === itemId);
}

// Reserve stock for an item in Redis
function reserveStockById(itemId, stock) {
  return client.set(`item.${itemId}`, stock);
}

// Function to get the current reserved stock by item ID
async function getCurrentReservedStockById(itemId) {
  const reservedStock = await getAsync(`item.${itemId}`);
  return reservedStock ? parseInt(reservedStock, 10) : 0;
}

// Route to get the list of available products
app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

// Route to get product details including current available stock
app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const item = getItemById(itemId);

  if (item) {
    const currentReservedStock = await getCurrentReservedStockById(itemId);
    item.currentQuantity = item.initialAvailableQuantity - currentReservedStock;
    res.json(item);
  } else {
    res.status(404).json({ status: 'Product not found' });
  }
});

// Route to reserve a product
app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const item = getItemById(itemId);

  if (!item) {
    res.status(404).json({ status: 'Product not found' });
  } else {
    const currentReservedStock = await getCurrentReservedStockById(itemId);

    if (currentReservedStock < item.initialAvailableQuantity) {
      reserveStockById(itemId, currentReservedStock + 1);
      res.json({ status: 'Reservation confirmed', itemId });
    } else {
      res.json({ status: 'Not enough stock available', itemId });
    }
  }
});

app.listen(port, () => {
  console.log(`Server is listening on port ${port}`);
});
