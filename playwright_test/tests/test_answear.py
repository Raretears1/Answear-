import pytest
from playwright_test.page_objects.page_model import *


class TestAnswearAdult:
    @pytest.mark.parametrize('gender', ['male', 'female'])
    def test_red_vans(self, open_link, gender):
        print(f'PARAMETRIZATION gender: {gender}')
        answear_page = AnswearAdult(open_link, gender)
        answear_page.go_to_red_vans_for_adult()
        print(f'ANSWEAR gender: {answear_page.gender}')
        answear_page.page.close()


class TestAnswearKidGirl:
    @pytest.mark.parametrize('gender', ['solo_girl'])
    def test_pink_converse(self, open_link, gender):
        print(f'PARAMETRIZATION gender: {gender}')
        answear_page = AnswearKidGirl(open_link, gender)
        answear_page.go_to_pink_converse_for_kid_girl()
        print(f'ANSWEAR gender: {answear_page.gender}')
        answear_page.page.close()


class TestAnswearKidBoy:
    @pytest.mark.parametrize('gender', ['boy'])
    def test_favorites_to_boy(self, open_link, gender):
        print(f'PARAMETRIZATION gender: {gender}')
        answear_page = AnswearKidBoy(open_link, gender)
        answear_page.favorites_shoes_for_boy()
        print(f'ANSWEAR gender: {answear_page.gender}')
        answear_page.page.close()


class TestAnswearKids:
    @pytest.mark.parametrize('gender', ['boy', 'girl'])
    def test_first_sale_position_for_kids(self, open_link, gender):
        print(f'PARAMETRIZATION gender: {gender}')
        answear_page = AnswearKids(open_link, gender)
        answear_page.go_to_first_sale_position()
        print(f'ANSWEAR gender: {answear_page.gender}')
        answear_page.page.close()
