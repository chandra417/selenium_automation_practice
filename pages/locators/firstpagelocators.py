from selenium.webdriver.common.by import By

class AddressLocators:
    enter_name = (By.ID, "name")
    enter_email = (By.ID, "email")
    enter_phone = (By.ID, "phone")
    enter_address = (By.ID, "textarea")

class CheckboxLocators:
    select_male = (By.ID, "male")
    select_female = (By.ID, "female")
    select_days = (By.XPATH, "//input[contains(@id, 'day')]")

class DropdownLocators:
    select_country = (By.ID, "country")
    select_colors = (By.ID, "colors")
    select_animals = (By.ID, "animals")

class HandlingTabsLocators:
    wiki_search_bar = (By.ID, "Wikipedia1_wikipedia-search-input")
    wiki_search_button = (By.CLASS_NAME, "wikipedia-search-button")
    search_results = (By.XPATH, "//div[@class='wikipedia-search-results']//a")
    new_tab = (By.XPATH, "//button[contains(text(), 'New Tab')]")
    popup_window = (By.ID, "PopUp")

class DynamicLocators:
    dynamic_button = (By.XPATH, "//button[@onclick='toggleButton(this)']")

class AlertsAndPopupsLocators:
    simple_alert = (By.ID, "alertBtn")
    confirm_alert = (By.ID, "confirmBtn")
    after_confirm_alert = (By.ID, "demo")
    prompt_alert = (By.ID, "promptBtn")

class MouseHoverLocators:
    mouse_hover = (By.XPATH, "//*[@id='HTML3']/div[1]/div")
    mouse_hover_laptops = (By.XPATH, "(//div[@class='dropdown-content']/a)[2]")
    double_click = (By.XPATH, "//button[@ondblclick='myFunction1()']")
    field_1 = (By.ID, "field1")
    field_2 = (By.ID, "field2")

class DragAndDropLocators:
    source = (By.ID, "draggable")
    destination = (By.ID, "droppable")
    slide_start = (By.XPATH, "//span[@tabindex='0'][1]")
    slide_end = (By.XPATH, "//span[@tabindex='0'][2]")

    scroll_down = (By.ID, "comboBox")
    scroll_down_list = (By.XPATH, "//*[@id='dropdown']/div[26]")

class HandlingPaginationTabel:
    pages = (By.XPATH, "//ul[@id='pagination']/li/a")
    names_in_each_page = (By.XPATH, "//table[@id='productTable']/tbody/tr/td[2]")