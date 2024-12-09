from behave import given, then


@given('I send a GET request to "{endpoint}" with the query "{query}"')
def step_impl(context, endpoint, query):
    context.search.send_request_to_endpoint(endpoint, query)


@given('I send a GET request to "search" for book with the title "{book}"')
def step_impl(context, book):
    context.search.send_request_for_book_with_title(book)


@then('The response status code should be {status_code}')
def step_impl(context, status_code):
    assert context.search.check_status_code(int(status_code))


@then('The response should contain {number} of results')
def step_impl(context, number):
    assert context.search.check_number_of_results(number)


@then('The first result in response should have the title {book_title}')
def step_impl(context, book_title):
    assert context.search.check_first_title_in_results(book_title)
