@api @search
Feature: API Testing

  Scenario Outline: Validate number of results for authors search
    Given I send a GET request to "authors.json" with the query "<name>"
    Then The response status code should be 200
    And The response should contain <number> of results
    Examples:
      | name         | number |
      | Stephen King | 82     |
      | J K Rowling  | 5      |

  Scenario Outline: Validate first result for book title search
    Given I send a GET request to "search" for book with the title "<book>"
    Then The response status code should be 200
    And The first result in response should have the title <book_title>
    Examples:
      | book          | book_title                               |
      | Harry Potter  | Harry Potter and the Philosopher's Stone |
      | War and peace | War and Peace                            |