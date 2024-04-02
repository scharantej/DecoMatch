## Flask Application Design

### HTML Files

**index.html:**
- The main landing page of the application.
- Displays a form for clients to input their project details and preferences.

**designers.html:**
- A page listing all the registered interior designers on the platform.
- Provides information about each designer's specialization, location, and previous projects.

**projects.html:**
- A page showcasing the ongoing and completed projects on the platform.
- Includes details like project timeline, budget, and client feedback.

**marketplace.html:**
- The marketplace page where clients can browse and purchase furniture, décor, and other design elements.
- Provides options for filtering and sorting products.

### Routes

**@app.route('/')**
- The route for the index page.
- Displays the form for clients to submit their project requirements.

**@app.route('/designers')**
- The route for the designers page.
- Lists all the registered interior designers on the platform.

**@app.route('/projects')**
- The route for the projects page.
- Showcases the ongoing and completed projects on the platform.

**@app.route('/marketplace')**
- The route for the marketplace page.
- Displays the products available for purchase.

**@app.route('/submit_project', methods=['POST'])**
- The route for handling form submissions from the index page.
- Stores the client's project details and preferences.

**@app.route('/match_designer')**
- The route for matching clients with interior designers.
- Uses the client's project details to find the most suitable designers.

**@app.route('/designer/<designer_id>')**
- The route for viewing an individual interior designer's profile.
- Displays the designer's portfolio, contact information, and reviews.