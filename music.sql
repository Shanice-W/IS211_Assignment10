CREATE TABLE artist (
    id INTEGER PRIMARY KEY,
    artist TEXT,
);

CREATE TABLE album (
    id INTEGER PRIMARY KEY,
    album TEXT,
    artistID INTEGER,
);

CREATE TABLE song (
    id INTEGER PRIMARY KEY,
    song TEXT,
    artistID INTEGER,
    albumID INTEGER,
    trackNum INTEGER,
    trackLen INTEGER
);