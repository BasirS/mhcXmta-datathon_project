-- FAIR FARES SUBWAY RIDERSHIP ANALYSIS QUERIES

-- NETWORK ANALYSIS QUERIES
WITH station_connections AS (
    SELECT 
        s1.station_complex as source_station,
        s2.station_complex as target_station,
        COUNT(*) as connection_frequency,
        AVG(s1.transfers) as average_transfers
    FROM subway_rides s1
    JOIN subway_rides s2 
        ON s1.transit_timestamp = s2.transit_timestamp
        AND s1.station_complex != s2.station_complex
    WHERE s1.transfers > 0
    GROUP BY s1.station_complex, s2.station_complex
)
SELECT * FROM station_connections;

-- TEMPORAL PATTERN QUERIES
WITH hourly_patterns AS (
    SELECT 
        EXTRACT(HOUR FROM transit_timestamp) as hour,
        SUM(ridership) as total_rides,
        SUM(CASE WHEN fare_class_category LIKE '%Fair Fare%' 
            THEN ridership ELSE 0 END) as fair_fares_rides
    FROM subway_rides
    GROUP BY EXTRACT(HOUR FROM transit_timestamp)
)
SELECT * FROM hourly_patterns;

-- INTEGRATION ANALYSIS QUERIES
WITH modal_integration AS (
    SELECT 
        station_complex,
        DATE(transit_timestamp) as date,
        SUM(ridership) as total_rides,
        AVG(transfers) as avg_transfers
    FROM subway_rides
    WHERE fare_class_category LIKE '%Fair Fare%'
    GROUP BY station_complex, DATE(transit_timestamp)
)
SELECT * FROM modal_integration;