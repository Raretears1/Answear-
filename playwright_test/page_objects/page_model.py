import allure
from datetime import datetime
from playwright.sync_api import Page, expect
from playwright_test.base_vars.bv_for_reg import ANSWEAR_URL_KIDS, ANSWEAR_URL
from playwright_test.connect_to_db.connect import connect_to_db


class Answear:
    def __init__(self, page: Page, gender: str):
        self.page = page
        self.gender = gender
        self.screen_dir = ''
        self.db_gender = ''

    @allure.step
    def basic_response(self):
        response = self.page.request.get(f'{ANSWEAR_URL}')
        expect(response).to_be_ok()

    # Take a screenshot
    @allure.step
    def make_scr(self):
        self.page.screenshot(path=f'screen/{self.screen_dir}/screenshot_{self.current_time()}.png')

    # Return a timedate (screenshot)
    @staticmethod
    @allure.step
    def current_time() -> str:
        now = datetime.now()
        time = now.strftime("%H_%M_%S")
        return time

    # ADULT/CHILD CHOOSE SHOES
    @allure.step
    def choose_snickers(self):
        self.page.get_by_role("link", name="Взуття", exact=True).first.hover()
        self.page.get_by_role("link", name="Кеди").first.click()

    @allure.step
    def close_the_offer_card(self):
        if self.page.locator(".Modal__close__C40RR > .icon").is_visible():
            self.page.locator(".Modal__close__C40RR > .icon").click()


class AnswearAdult(Answear):

    def __init__(self, page: Page, gender: str):
        super().__init__(page, gender)
        if self.gender == 'male':
            self.screen_dir = 'male'
            self.db_gender = 'male'
        elif self.gender == 'female':
            self.screen_dir = 'female'
            self.db_gender = 'female'

    # RED VANS FOR ADULT
    @allure.step
    def go_to_red_vans_for_adult(self):
        self.basic_response()
        if self.gender == 'male':
            self.page.goto('https://answear.ua/k/vin')
        elif self.gender == 'female':
            self.page.goto('https://answear.ua/c/vona')
        self.red_vans_for_adult()
        self.make_scr()
        connect_to_db(self.db_gender)

    @allure.step
    def red_vans_for_adult(self):
        self.choose_snickers()
        self.filters_for_red_vans()
        self.choose_model_vans()
        self.add_to_cart_vans()
        self.check_cart_adult_vans()

    # Red vans for adult
    @allure.step
    def filters_for_red_vans(self):
        self.page.locator("[data-test=\"productBrand_filters\"]").get_by_text("Бренд").click()
        self.page.locator("#baseSearch").fill("vans")
        self.page.locator("[data-test=\"productBrand_filters\"]").get_by_text("Vans").click()
        expect(self.page.locator("[data-test=\"productBrand_filters\"]")).to_be_visible()
        self.page.locator("[data-test=\"productBrand_filters\"]").get_by_role("button", name="Ок").click()
        self.page.get_by_text("Розмір").click()
        self.page.get_by_role("listitem").filter(has_text="42").first.click()
        self.page.get_by_role("button", name="Ок").click()
        self.page.locator("[data-test=\"color_filters\"] div").click()
        self.page.get_by_role("listitem").filter(has_text="червоний").click()
        self.page.locator("[data-test=\"color_filters\"]").get_by_role("button", name="Ок").click()

    @allure.step
    def choose_model_vans(self):
        vans_locator = self.page.get_by_role("link", name="Товар: Кеди Vans Ua Old Skool: Кеди Vans Ua Old Skool")
        while not vans_locator.is_visible():
            self.page.mouse.wheel(delta_x=0, delta_y=400)
        vans_locator.click()

    @allure.step
    def add_to_cart_vans(self):
        self.page.get_by_role("button", name="Додати у Кошик").click()
        self.page.get_by_role("listitem").filter(has_text="42").click()

    @allure.step
    def check_cart_adult_vans(self):
        shoes_locator = [".CartItem__cartItemRow__jG5Ns", ".CartItem__cartItem__EZXu4"]
        self.page.locator("[data-test=\"cart_icon\"]").click()
        if self.gender == 'male':
            expect(self.page.locator(f"{shoes_locator[0]}").first).to_be_visible()
        elif self.gender == 'female':
            expect(self.page.locator(f"{shoes_locator[1]}").first).to_be_visible()
        self.close_the_offer_card()


class AnswearKidGirl(Answear):
    def __init__(self, page: Page, gender: str):
        super().__init__(page, gender)
        self.gender = 'solo_girl'
        self.screen_dir = 'girl'
        self.db_gender = 'solo_girl'

    # PINK CONVERSE FOR KID
    @allure.step
    def go_to_pink_converse_for_kid_girl(self):
        self.basic_response()
        self.gender = 'solo_girl'
        self.page.goto(f'{ANSWEAR_URL_KIDS}')
        self.pink_converse_for_kid_girl()
        self.make_scr()
        connect_to_db(self.db_gender)

    @allure.step
    def pink_converse_for_kid_girl(self):
        self.choose_snickers()
        self.filters_for_converse()
        self.choose_model_converse()
        self.add_to_cart_converse()
        self.add_to_cart_new_converse()
        self.check_cart_child_converse()

    # Child pink Converse
    @allure.step
    def filters_for_converse(self):
        self.close_the_offer_card()
        self.page.locator("[data-test=\"productBrand_filters\"] div").click()
        self.page.locator("#baseSearch").click()
        self.page.locator("#baseSearch").fill("Converse")
        self.page.locator("[data-test=\"productBrand_filters\"]").get_by_text("Converse").click()
        self.page.locator("[data-test=\"productBrand_filters\"]").get_by_role("button", name="Ок").click()
        self.page.locator("[data-test=\"size_filters\"] div").click()
        self.page.get_by_role("listitem").filter(has_text="33").first.click()
        self.page.get_by_role("button", name="Ок").click()

    @allure.step
    def choose_model_converse(self):
        converse_locator = self.page.get_by_text("Converse - Дитячі кеди Chuck Taylor All Star")
        while not converse_locator.is_visible():
            self.page.mouse.wheel(delta_x=0, delta_y=50)
        converse_locator.click()

    @allure.step
    def add_to_cart_converse(self):
        self.page.get_by_role("button", name="Додати у Кошик").click()
        self.page.get_by_role("listitem").filter(has_text="27").click()

    @allure.step
    def add_to_cart_new_converse(self):
        self.choose_snickers()
        self.filters_for_converse()
        converse_locator = self.page.get_by_text("Дитячі кеди Converse Chuck 70 Sweet Scoops").nth(1)
        while not converse_locator.is_visible():
            self.page.mouse.wheel(delta_x=0, delta_y=500)
        converse_locator.click()
        self.page.get_by_role("button", name="Додати у Кошик").click()
        self.page.get_by_role("listitem").filter(has_text="28").first.click()

    @allure.step
    def check_cart_child_converse(self):
        self.page.locator("[data-test=\"cart_icon\"]").click()
        expect(self.page.locator(".CartItem__cartItemRow__jG5Ns") and self.page.locator(".CartItem__cartItem__"
                                                                                        "EZXu4").first).to_be_visible()
        self.close_the_offer_card()


class AnswearKidBoy(Answear):

    def __init__(self, page: Page, gender: str):
        super().__init__(page, gender)
        self.gender = 'boy'
        self.screen_dir = 'boy'

    @allure.step
    def favorites_shoes_for_boy(self):
        self.basic_response()
        self.gender = 'boy'
        self.page.goto(f'{ANSWEAR_URL_KIDS}')
        self.go_to_kid_shoes()
        self.make_scr()

    @allure.step
    def go_to_kid_shoes(self):
        self.page.get_by_role("link", name="Взуття", exact=True).hover()
        self.page.get_by_role("link", name="Кросівки", exact=True).nth(1).click()
        self.go_to_kid_shoes_filters()

    @allure.step
    def go_to_kid_shoes_filters(self):
        self.page.locator("[data-test=\"productBrand_filters\"] div").click()
        self.page.locator("#baseSearch").fill("Nike Kids")
        self.page.locator("[data-test=\"productBrand_filters\"]").get_by_role("listitem").click()
        self.page.locator("#baseSearch").click()
        self.page.locator("#baseSearch").fill("Puma")
        self.page.locator("[data-test=\"productBrand_filters\"]").get_by_role("listitem").click()
        self.page.locator("[data-test=\"productBrand_filters\"]").get_by_role("button", name="Ок").click()
        self.page.locator("[data-test=\"size_filters\"] div").click()
        # self.page.get_by_role("listitem").filter(has_text="30").first.click()
        self.page.locator("#baseSearch").fill("30")
        self.page.get_by_text("30", exact=True).first.click()
        self.page.get_by_role("button", name="Ок").click()
        self.page.locator("[data-test='add_to_fav']").nth(2).click()
        self.page.locator("[data-test=\"size_selector\"] div").filter(has_text="30").first.click()
        self.page.get_by_role("button", name="Ок").click()
        self.page.locator("[data-test=\"size_filters\"] div").click()
        self.page.get_by_role("listitem").filter(has_text="34").first.click()
        self.page.get_by_role("button", name="Ок").click()
        self.page.locator(
            "div:nth-child(4) > .ProductItem__productCard__8ivfZ > .ProductItem__productCardImageWrapper__8Is-g > "
            ".ProductItem__productCardFavouritesButtonWrapper__blFyN > .ProductItem__"
            "productCardFavouriteHeartButton__QU5wk").click()

        self.page.get_by_role("listitem").filter(has_text="35").click()
        self.page.get_by_role("button", name="Ок").click()
        self.page.locator("[data-test=\"fav_icon\"]").click()


class AnswearKids(Answear):

    def __init__(self, page: Page, gender: str):
        super().__init__(page, gender)
        if self.gender == 'boy':
            self.screen_dir = 'boy'
            self.db_gender = 'boy'
        elif self.gender == 'girl':
            self.screen_dir = 'girl'
            self.db_gender = 'girl'

    # FIRST SALE POSITION FOR KIDS
    @allure.step
    def go_to_first_sale_position(self):
        self.basic_response()
        if self.gender == 'boy':
            self.page.goto(f'{ANSWEAR_URL_KIDS}')
            self.sale_position_boy()
        elif self.gender == 'girl':
            self.page.goto(f'{ANSWEAR_URL_KIDS}')
            self.sale_position_girl()
        self.make_scr()
        connect_to_db(self.db_gender)

    @allure.step
    def sale_position_boy(self):
        self.main_way_to_kids_sale()
        self.boy_sale()

    @allure.step
    def sale_position_girl(self):
        self.main_way_to_kids_sale()
        self.girl_sale()

    # MAIN WAY TO kids sale
    @allure.step
    def main_way_to_kids_sale(self):
        self.page.get_by_role("link", name="діти", exact=True).click()
        self.page.get_by_role("link", name="Розпродаж").click()
        self.page.get_by_role("link", name="Answear logo").hover()

    #  Kids(boy) first sale position
    @allure.step
    def boy_sale(self):
        self.page.get_by_role("link", name="Хлопчик").click()
        self.close_the_offer_card()
        self.page.get_by_role("link", name="Товар: Дитячі штани Lemon Explore: Дитячі штани Lemon Explore").click()
        self.page.get_by_title("Блакитний").click()
        expect(self.page.get_by_role("img", name="блакитний Дитячі штани Lemon Explore Для хлопчиків").nth(1)). \
            to_be_visible()
        self.page.get_by_role("button", name="Додати у Кошик").click()
        self.page.get_by_role("listitem").filter(has_text="116").click()
        self.page.locator("[data-test=\"cart_icon\"]").click()
        expect(self.page.locator(".CartItem__cartItem__EZXu4").first).to_be_visible()

    #  Kids(girl) first sale position
    @allure.step
    def girl_sale(self):
        self.page.get_by_role("link", name="Дівчинка").click()
        self.close_the_offer_card()
        self.page.get_by_role("link", name="Товар: дитяча гірськолижна куртка Lemon Explore: дитяча гірськолижна куртка"
                                           " Lemon Explore").click()
        self.page.get_by_role("button", name="Додати у Кошик").click()
        self.page.get_by_role("listitem").filter(has_text="158").click()
        self.page.locator("[data-test=\"cart_icon\"]").click()
        expect(self.page.locator(".CartItem__cartItem__EZXu4").first).to_be_visible()
