# Weather Application - Replit.md

## Overview

This is a modern weather application built with a full-stack architecture using React/TypeScript frontend and Express.js backend. The application provides real-time weather data, forecasts, and location-based services with a clean, responsive user interface featuring glassmorphism design elements.

## System Architecture

### Frontend Architecture
- **Framework**: React 18 with TypeScript
- **Build Tool**: Vite for fast development and optimized builds
- **UI Library**: Radix UI components with shadcn/ui styling system
- **Styling**: Tailwind CSS with custom weather-themed color variables
- **State Management**: TanStack Query for server state management
- **Routing**: Wouter for lightweight client-side routing

### Backend Architecture
- **Runtime**: Node.js with Express.js framework
- **API Design**: RESTful API endpoints for weather data
- **Database**: PostgreSQL with Drizzle ORM for type-safe database operations
- **Session Storage**: PostgreSQL-backed sessions using connect-pg-simple
- **Development**: Hot reloading with Vite middleware integration

## Key Components

### Weather Services
- **Current Weather**: Real-time weather data from OpenWeatherMap API
- **5-Day Forecast**: Extended weather predictions with 3-hour intervals
- **Air Quality Index**: Environmental air quality data
- **Geocoding**: Location search and coordinate resolution
- **Geolocation**: Browser-based location detection

### UI Components
- **Weather Header**: Search interface with location autocomplete
- **Current Weather**: Main weather display with temperature, conditions, and details
- **Hourly Forecast**: 24-hour weather timeline with 3-hour intervals
- **Weekly Forecast**: 5-day weather overview with min/max temperatures
- **Additional Info**: Sunrise/sunset, air quality, visibility, and other metrics

### Database Schema
- **Users Table**: User authentication and profile management (id, username, password)
- **Weather Locations**: Cached location data for faster lookups (id, name, country, lat, lon, state)
- **Schema Validation**: Zod schemas for runtime type checking
- **Storage Layer**: Flexible IStorage interface with DatabaseStorage and MemStorage implementations
- **Database Connection**: Neon PostgreSQL with Drizzle ORM and connection pooling

## Data Flow

1. **Location Detection**: App attempts geolocation, falls back to manual search
2. **Weather Data Fetching**: Parallel API calls to OpenWeatherMap for current, forecast, and air quality data
3. **Data Caching**: TanStack Query provides intelligent caching with 10-minute stale time
4. **UI Updates**: Reactive updates based on location changes and data refresh
5. **Error Handling**: Graceful fallbacks for API failures and permission denials

## External Dependencies

### Core APIs
- **OpenWeatherMap API**: Primary weather data provider
  - Current Weather API
  - 5-Day/3-Hour Forecast API
  - Air Pollution API
  - Geocoding API

### Database
- **Neon Database**: Serverless PostgreSQL for production
- **Drizzle ORM**: Type-safe database operations and migrations

### UI Libraries
- **Radix UI**: Accessible, unstyled component primitives
- **Lucide React**: Icon library for weather-themed icons
- **Embla Carousel**: Touch-friendly carousels for forecast data

## Deployment Strategy

### Development
- **Local Development**: Vite dev server with Express API integration
- **Hot Reloading**: Real-time updates for both frontend and backend
- **Environment Variables**: Separate configs for development and production

### Production Build
- **Frontend**: Vite builds optimized static assets
- **Backend**: esbuild bundles Express server for deployment
- **Database Migrations**: Drizzle Kit handles schema migrations
- **Environment**: Production-ready with proper error handling

### Hosting
- **Frontend & Backend**: Single deployment with Express serving static files
- **Database**: Neon serverless PostgreSQL
- **API Keys**: Secure environment variable management

## Changelog

```
Changelog:
- July 03, 2025. Initial setup
- January 03, 2025. Added database support with PostgreSQL and Drizzle ORM
- January 03, 2025. Implemented DatabaseStorage class with fallback to MemStorage
```

## User Preferences

```
Preferred communication style: Simple, everyday language.
```

## Database Setup

### Current State
- **Storage**: Currently using in-memory storage (MemStorage) with pre-populated city data
- **Database Ready**: Complete PostgreSQL schema and DatabaseStorage implementation available
- **Auto-fallback**: App automatically uses memory storage if no database is configured

### To Enable Database Storage
1. **Create Neon Database**: 
   - Go to https://neon.tech and create a free account
   - Create a new project and database
   - Copy the connection string

2. **Add Database URL**:
   - In Replit Secrets, add `DATABASE_URL` with your Neon connection string
   - Format: `postgresql://user:password@host/database?sslmode=require`

3. **Run Migration**:
   ```bash
   npm run db:push
   ```

4. **Restart Application**: The app will automatically detect the database and switch to DatabaseStorage

### Database Features
- **User Management**: Store and retrieve user accounts
- **Location Caching**: Save frequently searched locations for faster access
- **Type Safety**: Full TypeScript support with Drizzle ORM
- **Migration Support**: Schema changes handled through Drizzle Kit

## Additional Notes

### Key Features
- **Responsive Design**: Mobile-first approach with progressive enhancement
- **Accessibility**: Proper ARIA labels and keyboard navigation
- **Performance**: Optimized loading with skeleton states and progressive enhancement
- **Error Boundaries**: Graceful error handling with user-friendly messages
- **Temperature Units**: Celsius/Fahrenheit toggle with persistent preferences

### Architecture Decisions
- **Monorepo Structure**: Shared types and schemas between frontend and backend
- **Type Safety**: End-to-end TypeScript with runtime validation
- **Component Composition**: Modular, reusable components with clear interfaces
- **API Design**: RESTful endpoints with consistent error responses
- **Caching Strategy**: Smart caching to minimize API calls while ensuring fresh data

The application prioritizes user experience with fast loading times, intuitive navigation, and comprehensive weather information in a visually appealing interface.