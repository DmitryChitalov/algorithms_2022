from collections import namedtuple

COMPANIES_TEMPL = namedtuple('Companies', 'prof_quart_1 prof_quart_2 prof_quart_3 prof_quart_4')
company = COMPANIES_TEMPL(
            prof_quart_1 = 100,
            prof_quart_2 = 200,
            prof_quart_3 = 300,
            prof_quart_4 = 400
        )
print(company)