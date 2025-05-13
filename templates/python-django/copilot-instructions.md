# Copilot Instructions

This document provides comprehensive guidelines for generating code using GitHub Copilot in our project. The instructions combine best practices with our specific requirements and default tech stack.

## Objectives
- Generate clear, maintainable, and testing-friendly code.
- Ensure the code includes thorough documentation and data type declarations.
- Encourage the use of primary logging for printing events.
- Produce comprehensive tests with new classes.

## Guidelines

### 1. Documentation and Comments
- Every class and method must have comments explaining their purpose and functionality.
  - Example:
    ```python
    # A class representing a data processor.
    class DataProcessor:
        # Initializes the DataProcessor with initial configuration.
        def __init__(self, config: dict) -> None:
            """
            Initialize with configuration settings.
            
            :param config: Dictionary containing configuration parameters.
            """
            self.config = config
    ```

### 2. Data Type Declarations
- Methods and functions must declare the data types for both parameters and return values.
  - Example:
    ```python
    def add_numbers(a: int, b: int) -> int:
        """
        Adds two integers and returns the sum.
        
        :param a: First integer.
        :param b: Second integer.
        :return: The sum of a and b.
        """
        return a + b
    ```
- Metrics class inheritance of Metric class:
  - All new metrics should inherit from the base Metric class.
  - Ensure that the new metrics class implements all required methods and properties.
    - Example:
      ```python
      class CustomMetric(Metric):
          def calculate(self) -> float:
              # Custom calculation logic
              pass
      ```

### 3. Django application architecture

- Follow the MTV (Model-Template-View) pattern strictly
  - Models: Data structure and business logic
  - Templates: Presentation logic only
  - Views: Handle HTTP requests and responses
- Views and templates should be separated
- Views should not contain any business logic
- Create service layers for complex business logic
- Data for charts or tables should be fetched via AJAX calls and API endpoints (under `/api/` context)
- All data should be fetched from the database and never hardcoded
- Use Django forms for data validation and cleaning
- Leverage Django's class-based views when appropriate

### 4. Testing Friendly Code
- Code should be written in a manner that facilitates unit testing.
- Separate business logic from UI and external dependencies.
- Use dependency injection where possible to make testing easier.
- EVERY API ENDPOINT MUST HAVE TEST CASES
- Use factories (e.g., factory_boy) for test data generation
- Use fixtures for common test data setups

### 5. Test Creation with New Classes
- Create separate test classes for new code. These tests should cover different scenarios and edge cases.
- Place tests in designated test files or directories.
- Use a consistent naming convention for test files (e.g., `test_<module_name>_<test_type>.py`).
- SPLIT TESTS INTO MOCK AND INTEGRATION TESTS. NEVER COMBINE THEM INTO ONE FILE
- Set up data before running tests to ensure a clean state.
- Example (using Django's TestCase):
  ```python
  from django.test import TestCase
  from django.urls import reverse
  from myapp.models import MyModel
  
  class MyModelIntegrationTest(TestCase):
      def setUp(self):
          # Set up test data
          self.test_item = MyModel.objects.create(name="Test Item", value=10)
      
      def test_model_creation(self):
          # Test model creation and retrieval
          self.assertEqual(MyModel.objects.count(), 1)
          self.assertEqual(MyModel.objects.first().name, "Test Item")
      
      def test_view_response(self):
          # Test view response with the model
          response = self.client.get(reverse('mymodel-detail', kwargs={'pk': self.test_item.pk}))
          self.assertEqual(response.status_code, 200)
          self.assertContains(response, "Test Item")
  ```

### 6. Primary Logging for Printing Events
- Use Django's logging system instead of print statements.
- Configure logging properly in settings.py:
  ```python
  LOGGING = {
      'version': 1,
      'disable_existing_loggers': False,
      'formatters': {
          'verbose': {
              'format': '{levelname} {asctime} {module} {message}',
              'style': '{',
          },
      },
      'handlers': {
          'console': {
              'class': 'logging.StreamHandler',
              'formatter': 'verbose',
          },
          'file': {
              'class': 'logging.FileHandler',
              'filename': 'django.log',
              'formatter': 'verbose',
          },
      },
      'loggers': {
          'django': {
              'handlers': ['console', 'file'],
              'level': 'INFO',
          },
          'myapp': {
              'handlers': ['console', 'file'],
              'level': 'DEBUG',
              'propagate': True,
          },
      },
  }
  ```
- Use appropriate log levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)
- Example of proper logging in views:
  ```python
  import logging
  
  logger = logging.getLogger(__name__)
  
  def my_view(request):
      logger.info(f"Processing request from user {request.user}")
      try:
          # Process request
          result = process_data()
          logger.debug(f"Processed data: {result}")
          return render(request, 'template.html', {'result': result})
      except Exception as e:
          logger.error(f"Error processing request: {e}", exc_info=True)
          return HttpResponseServerError("An error occurred")
  ```

### 7. Data Visualization
- Use Chart.js for data visualization.
- Keep JavaScript code separate from HTML.
- Use Django's template system to pass data to the frontend:
  ```python
  # views.py
  def chart_view(request):
      data = get_chart_data()  # Get data from service or model
      return render(request, 'chart_template.html', {'chart_data': json.dumps(data)})
  ```
- Implement API endpoints for dynamic data loading:
  ```python
  # views.py
  from django.http import JsonResponse
  
  def chart_data_api(request):
      data = get_chart_data()
      return JsonResponse(data)
  ```
- Structure JavaScript properly:
  ```javascript
  // chart_script.js
  document.addEventListener('DOMContentLoaded', function() {
      const ctx = document.getElementById('myChart').getContext('2d');
      
      // Fetch data from API
      fetch('/api/chart-data/')
          .then(response => response.json())
          .then(data => {
              new Chart(ctx, {
                  type: 'bar',
                  data: data,
                  options: {
                      responsive: true,
                      // Other configuration options
                  }
              });
          })
          .catch(error => console.error('Error loading chart data:', error));
  });
  ```

### 8. Security Best Practices
- Always validate and sanitize input parameters from URLs, forms, and APIs.
- Use Django's built-in mechanisms to prevent common vulnerabilities:
  - Always use CSRF tokens in forms: `{% csrf_token %}`
  - Use Django's ORM instead of raw SQL queries
  - Use `get_object_or_404()` rather than handling exceptions manually
  - Implement proper permission checks using Django's authentication system
- Protect against common attacks:
  - XSS: Django templates auto-escape by default; keep this enabled
  - CSRF: Use Django's CSRF middleware and tokens
  - SQL Injection: Use ORM and parameterized queries
  - Clickjacking: Set proper X-Frame-Options headers
  - Include security-related headers:
    ```python
    # settings.py
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_BROWSER_XSS_FILTER = True
    X_FRAME_OPTIONS = 'DENY'
    CSRF_COOKIE_SECURE = True  # for HTTPS sites
    SESSION_COOKIE_SECURE = True  # for HTTPS sites
    ```
- Never trust user input; use Django forms for validation:
  ```python
  from django import forms
  
  class UserInputForm(forms.Form):
      name = forms.CharField(max_length=100)
      email = forms.EmailField()
      age = forms.IntegerField(min_value=0, max_value=120)
      
      def clean_name(self):
          """Custom validation for name field"""
          name = self.cleaned_data['name']
          # Custom validation logic
          return name
  ```

## Default Tech Stack
- **Python 3.9+**: For backend logic and scripting.
- **Django 4.2+**: For web framework and REST API.
  - Django REST Framework for API development
  - Django Debug Toolbar for development environment
- **PostgreSQL/SQLite**: PostgreSQL for production, SQLite for development.
- **Frontend**:
  - Chart.js: For data visualization.
  - jQuery 3.x: For DOM manipulation and AJAX requests.
  - Bootstrap 5: For responsive design and UI components.
  - ES6+ JavaScript: Modern JavaScript syntax with optional TypeScript
- **Testing**:
  - pytest: For efficient test running
  - factory_boy: For test data generation
  - coverage: For measuring test coverage
- **Development Tools**:
  - Docker/Docker Compose: For consistent development environments
  - pre-commit hooks: For code quality checking
  - black/flake8/isort: For code formatting and linting

## Coding Style and Best Practices
- **Follow PEP 8**: Python code should follow PEP 8 style guide
- **Modularity**: Write modular code that is easier to maintain and test.
- **DRY (Don't Repeat Yourself)**: Reuse code when possible through inheritance and composition.
- **Consistency**: Follow consistent naming conventions and coding standards.
- **Django-specific conventions**:
  - Use plural names for app directories
  - Use singular names for models
  - Use plural names for views, templates, and URLs that return multiple objects
  - Use singular names for views, templates, and URLs that return single objects
- **Error Handling**: Implement robust exception handling with appropriate error messages.
- **Comments and Documentation**:
  - Use docstrings for classes and methods
  - Comment complex algorithms and logic
  - Use type hints consistently

## Common Pitfalls to Avoid

- **Avoid code duplication:** Reuse functions and classes instead of copying code.
  - **Bad:**
    ```python
    def foo():
        print("Hello")
    def bar():
        print("Hello")
    ```
  - **Good:**
    ```python
    def greet():
        print("Hello")
    ```

- **Avoid business logic in views:** Keep business logic in service or model layers.
  - **Bad:**
    ```python
    def product_view(request):
        # Business logic in view (bad practice)
        products = Product.objects.all()
        total_value = sum(p.price * p.quantity for p in products)
        return render(request, 'products.html', {'products': products, 'total': total_value})
    ```
  - **Good:**
    ```python
    # models.py or services.py
    class ProductService:
        @staticmethod
        def get_products_with_total():
            products = Product.objects.all()
            total_value = sum(p.price * p.quantity for p in products)
            return products, total_value
    
    # views.py
    def product_view(request):
        products, total = ProductService.get_products_with_total()
        return render(request, 'products.html', {'products': products, 'total': total})
    ```

- **Avoid N+1 query problems:** Use `select_related` and `prefetch_related` for efficient querying.
  - **Bad:**
    ```python
    # This causes N+1 queries
    orders = Order.objects.all()
    for order in orders:
        print(order.customer.name)  # Separate query for each order's customer
    ```
  - **Good:**
    ```python
    # This performs a join, resulting in just 1 query
    orders = Order.objects.select_related('customer').all()
    for order in orders:
        print(order.customer.name)  # No additional queries
    ```

- **Avoid hardcoded data:** Always fetch data from the database or configuration.
  - **Bad:**
    ```python
    def get_categories():
        return ["Electronics", "Books", "Clothing"]
    ```
  - **Good:**
    ```python
    def get_categories():
        return Category.objects.values_list('name', flat=True)
    ```

- **Avoid mixing test types:** Keep mock tests and integration tests in separate files.

- **Avoid exposing sensitive information:** Never commit secrets or sensitive configuration.
  - **Bad:**
    ```python
    SECRET_KEY = 'actual-secret-key-here'
    DATABASE_PASSWORD = 'actual-db-password'
    ```
  - **Good:**
    ```python
    from decouple import config
    
    SECRET_KEY = config('SECRET_KEY')
    DATABASE_PASSWORD = config('DATABASE_PASSWORD')
    ```

- **Avoid direct template variable access without validation:** Always validate and sanitize data.
  - **Bad:**
    ```python
    # Directly passing user input to template
    def search_view(request):
        query = request.GET.get('q', '')
        return render(request, 'search.html', {'query': query})
    ```
  - **Good:**
    ```python
    # Validating user input
    from django import forms
    
    class SearchForm(forms.Form):
        q = forms.CharField(max_length=100, required=False)
    
    def search_view(request):
        form = SearchForm(request.GET)
        query = form.cleaned_data.get('q', '') if form.is_valid() else ''
        return render(request, 'search.html', {'query': query, 'form': form})
    ```

- **Avoid race conditions:** Use Django's transaction management and locking mechanisms.
  - **Bad:**
    ```python
    def transfer_funds(from_account, to_account, amount):
        if from_account.balance >= amount:
            from_account.balance -= amount  # Race condition possible here
            from_account.save()
            
            to_account.balance += amount
            to_account.save()
            return True
        return False
    ```
  - **Good:**
    ```python
    from django.db import transaction
    
    def transfer_funds(from_account_id, to_account_id, amount):
        with transaction.atomic():
            # Lock both accounts to prevent race conditions
            from_account = Account.objects.select_for_update().get(id=from_account_id)
            to_account = Account.objects.select_for_update().get(id=to_account_id)
            
            if from_account.balance >= amount:
                from_account.balance -= amount
                from_account.save()
                
                to_account.balance += amount
                to_account.save()
                return True
            return False
    ```

By following these guidelines and best practices, you'll create Django applications that are maintainable, secure, and perform well.

