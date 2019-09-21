import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_open_catalogue_page_and_check_add_button_exist(browser):
	browser.get(link)

	add_btn = browser.find_element_by_css_selector('.btn-add-to-basket')
	assert add_btn.is_displayed() and add_btn.is_enabled(), print('Add button isn\'t presented')

	time.sleep(30)
