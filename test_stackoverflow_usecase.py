from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from test_helper import XpathVariables


def test_stack_overflow():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)

    # Navigate to google.com and search for "stackoverflow"
    driver.get("https://www.google.com")

    search_box_element_name = "q"
    search_box = driver.find_element_by_name(search_box_element_name)
    search_box.send_keys("stackoverflow")
    search_box.send_keys(Keys.RETURN)

    # Click on the first result returned. This is official stack overflow site.
    driver.find_element_by_xpath(XpathVariables.first_result).click()

    # Click on the left hamburger menu.
    driver.find_element_by_xpath(XpathVariables.hamburger_menu).click()

    # Click on the "Tags" link.
    driver.find_element_by_xpath(XpathVariables.tags_link).click()

    # Type 'python' into the 'filter by tag name' search bar.
    filter_box_element_name = "tagfilter"
    filter_box = driver.find_element_by_name(filter_box_element_name)
    filter_box.send_keys("python")
    filter_box.send_keys(Keys.RETURN)
    # Verification point: Verify results contain 'python' as a substring.

    # Select python 3.6
    link_text = "python-3.6"
    driver.find_element_by_link_text(link_text).click()
    # Verification point: Verify result title or descriptions returned includes python 3.6.

    # Click the filter button.
    driver.find_element_by_xpath(XpathVariables.filter_button).click()

    # Click 'Most frequent' radio button.
    driver.find_element_by_xpath(XpathVariables.most_frequent_radio_button).click()

    # Click the 'Apply filter' button.
    driver.find_element_by_xpath(XpathVariables.apply_filter_button).click()
    # Verification point: What are the requirements for 'Most frequent'? If it is a combination of number
    # ... votes & number of views, then verify the top result meets that requirement.

    # Scroll down a tad.
    # TODO: Improvement - Scroll & poll. See 'todo' 2 & 3 below for more details.
    for i in range(3):
        driver.find_element_by_tag_name('body').send_keys(Keys.ARROW_DOWN)

    # Get the highest number of votes & the author for the highest number of votes then print.
    votes_num = driver.find_element_by_xpath(XpathVariables.votes)
    user_class_name = "user-details"
    user_name = driver.find_element_by_class_name(user_class_name).text.split()[0]
    print("The highest number of votes is %s for author %s." % (votes_num.text, user_name))
    # Verification point: Get all number of votes listed for results on page and verify the top result
    # ... is the highest number of votes.

    # Close the window
    driver.close()

    # TODO: Additional improvements that can be made if given more time -
    # 1. Stay away from XPATH as much as possible. Use element name, id, text when possible.
    # ...or use CSS selectors.
    # 2. Use Action chains to move to elements when in view for scrolling.
    # 3. Use explicit waits for tricky elements that take time to load.
    # 4. Implement assertions for verification.