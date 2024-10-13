# Dashboard Web Application

This project is a web-based dashboard for visualizing data using a Python backend and a React/Next.js frontend. The system will use Python for data analysis and chart generation, and Next.js for building a modern, dynamic user interface.

## Tools and Technologies

### Frontend:
- **Next.js**: A React-based framework that allows for server-side rendering (SSR) and static site generation (SSG), making it ideal for building performant and SEO-friendly dashboards.
- **React**: The JavaScript library for building dynamic user interfaces.
- **API Integration**: The frontend will interact with the backend through REST API calls to fetch processed data and charts.

### Backend:
- **Flask**: A lightweight Python web framework used to handle data processing and analysis, and to serve Bokeh charts through APIs.
- **Bokeh**: A Python library used for creating interactive visualizations. Bokeh will be used to generate both static and dynamic charts from the analyzed data.

## Project Architecture

### Frontend (Next.js + React):
- **Dynamic Dashboards**: The dashboard UI will be built using React components, and data will be fetched from the Flask API.
- **Data Fetching**: The Next.js pages will fetch chart data via API calls from the Python backend during server-side rendering or on-demand in the client browser.
- **Chart Rendering**: For Bokeh-generated charts, the HTML or JSON outputs will be fetched from Flask and rendered within React components using `dangerouslySetInnerHTML`.

### Backend (Flask + Bokeh):
- **Data Analysis**: Flask will process the raw data and generate the corresponding Bokeh visualizations.
- **API Endpoints**: Flask will expose API routes to serve the Bokeh charts either as static HTML or JSON for embedding in the frontend.
  - Example endpoint: `/api/charts/<chart_id>` – returns the generated Bokeh chart for a specific dataset.
- **Bokeh Server**: For highly interactive charts, a Bokeh server may be set up to handle live interactions, with Flask routing requests to it as needed.

## Workflow

1. **Data Processing in Python**:
   - Data will be analyzed using Python libraries, and Bokeh will generate the charts.
   - Flask will expose the processed data and Bokeh charts through a set of API routes.

2. **Frontend Integration**:
   - Next.js will fetch the charts from Flask’s API and render them in the React components.
   - The charts may be static (rendered as HTML) or interactive, depending on how they are created in Bokeh.

3. **Deployment**:
   - The frontend (Next.js) and backend (Flask) will be deployed as separate services, allowing the Python backend to focus on heavy computation and the frontend to focus on the user interface.
