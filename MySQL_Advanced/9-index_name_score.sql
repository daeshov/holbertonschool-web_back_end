--creates an index idx_name_first_score
CREATE INDEX idx_name_first_score ON names(LEFT(name, 1), LEFT(score, 1));
