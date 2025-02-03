-- TEMPORAL PATTERNS
WITH hourly_bus_patterns AS (
    SELECT 
        EXTRACT(HOUR FROM transit_timestamp) as hour,
        SUM(ridership) as total_rides,
        SUM(CASE WHEN fare_class_category LIKE '%Fair Fare%' 
            THEN ridership ELSE 0 END) as fair_fares_rides
    FROM bus_rides
    GROUP BY EXTRACT(HOUR FROM transit_timestamp)
),

-- INTEGRATION PATTERNS
bus_integration AS (
    SELECT 
        bus_route,
        DATE(transit_timestamp) as date,
        SUM(ridership) as total_rides,
        AVG(transfers) as avg_transfers
    FROM bus_rides
    WHERE fare_class_category LIKE '%Fair Fare%'
    GROUP BY bus_route, DATE(transit_timestamp)
),

-- ROUTE ANALYSIS QUERIES
route_patterns AS (
    SELECT 
        bus_route,
        COUNT(*) as total_trips,
        SUM(ridership) as total_ridership,
        AVG(CASE WHEN fare_class_category LIKE '%Fair Fare%' 
            THEN 1 ELSE 0 END) as fair_fares_percentage
    FROM bus_rides
    GROUP BY bus_route
)
SELECT * FROM route_patterns
UNION ALL
SELECT * FROM hourly_bus_patterns
UNION ALL
SELECT * FROM bus_integration;