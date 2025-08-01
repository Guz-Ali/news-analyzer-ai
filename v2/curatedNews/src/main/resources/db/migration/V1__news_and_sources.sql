CREATE TABLE sources (
    id UUID PRIMARY KEY,
    name TEXT NOT NULL,
    base_link TEXT NOT NULL,
    description TEXT
);

CREATE TABLE news (
    id UUID PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    link TEXT NOT NULL,
    date TIMESTAMP WITH TIME ZONE NOT NULL,
    generated_date TIMESTAMP WITH TIME ZONE NOT NULL,
    source_id UUID REFERENCES sources(id)
);