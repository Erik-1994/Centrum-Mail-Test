

class EmailTests:
    def test_login_email(self, web_driver, email_password, email_name):
        web_driver.get(
            "https://user.centrum.sk/?url=https%3A%2F%2Fmail.centrum.sk")
        username = web_driver.find_element_by_name("ego_user")
        username.send_keys(email_name)

        password = web_driver.find_element_by_name("ego_secret")
        password.send_keys(email_password)

        password.submit()

        assert "mail.centrum" in web_driver.current_url

    def test_send_email(self, web_driver, email_test_code):

        write_mail = web_driver.find_element_by_id("compose_button")
        write_mail.click()

        to = web_driver.find_element_by_id("smart_input_to")
        to.send_keys("test.pytests@gmail.com")

        subject = web_driver.find_element_by_id("subject_input")
        subject.send_keys(email_test_code)

        send = web_driver.find_element_by_id("qa_email_send_upper")
        send.click()

    def test_if_emial_was_sended(self, web_driver, email_test_code):

        link_to_sanded_mails = web_driver.get(
            "https://mail.centrum.sk/?fld=1")

        text_area = web_driver.find_element_by_id(
            "mail_list_frm").text

        assert email_test_code in text_area

    def test_search_email(self, web_driver, email_test_code):
        search_input = web_driver.find_element_by_name("s_fulltext")
        search_input.send_keys(email_test_code)

        web_driver.find_element_by_class_name("search-icon").click()

        list_object = web_driver.find_element_by_id("maillist")

        assert email_test_code in list_object.text
