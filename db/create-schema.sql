CREATE TABLE plane_frames (
    id SERIAL PRIMARY KEY,
    icao VARCHAR(4) NOT NULL,
    speed FLOAT,
    lat FLOAT,
    lon FLOAT,
    alt INTEGER,
    timestamp TIMESTAMP
);

CREATE INDEX ix_plane_frames_icao ON plane_frames (icao);
