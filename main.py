url = "https://www.linkedin.com/jobs/search/?currentJobId=2682830021&f_AL=true&f_E=2&geoId=103173899&keywords=data%20analyst&location=Kyiv%20City%2C%20Ukraine"
email = "samir.soudki@lau.edu"
password = "Summer2014?"

from selenium import webdriver
chrome_web_driver = "C:\\Users\\Lenovo\\Desktop\\samourou python\\chromedriver_win32\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_web_driver)
driver.get(url)
sign_in = driver.find_element_by_class_name("nav__button-secondary")
sign_in.click()
username = driver.find_element_by_name("session_key")
username.send_keys(email)
pass_ = driver.find_element_by_name("session_password")
pass_.send_keys(password)
sign_in_button = driver.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button')
sign_in_button.click()

all_listings = driver.find_elements_by_css_selector(".job-card-container--clickable")

for listing in all_listings:
    print("called")


    # Try to locate the apply button, if can't locate then skip the job.
    try:
        apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
        apply_button.click()

        submit_button = driver.find_element_by_css_selector("footer button")

        # If the submit_button is a "Next" button, then this is a multi-step application, so skip.
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()
            discard_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()

        # Once application completed, close the pop-up window.

        close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
        close_button.click()

    # If already applied to job or job is no longer accepting applications, then skip.
    except "NoSuchElementException":
        print("No application button, skipped.")
        continue



