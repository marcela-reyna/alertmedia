from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from test_helper import XpathVariables


def test_stackoverflow():
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

    # Select python 3.6
    link_text = "python-3.6"
    driver.find_element_by_link_text(link_text).click()
    # Verification point: Verify results returned only include python 3.6 results.

    # Click the filter button.
    driver.find_element_by_xpath(XpathVariables.filter_button).click()

    # Click most frequent radio button.
    driver.find_element_by_xpath(XpathVariables.most_frequent_radio_button).click()

    # Click the Apply filter button.
    driver.find_element_by_xpath(XpathVariables.apply_filter_button).click()
    # Verification point: Verify the top result contains the most number of votes.

    # Get the author with the highest number of votes and display the author and number of votes.
    # First, scroll down a tad.
    for i in range(3):
        driver.find_element_by_tag_name('body').send_keys(Keys.ARROW_DOWN)

    # Get the highest number of votes & the author for the highest number of votes then print.
    votes_num = driver.find_element_by_xpath(XpathVariables.votes)

    user_class_name = "user-details"
    user_name = driver.find_element_by_class_name(user_class_name).text.split()[0]
    print("The highest number of votes is %s for author %s." % (votes_num.text, user_name))

    # Close the window
    driver.close()