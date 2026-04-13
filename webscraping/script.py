from selenium import webdriver
from bs4 import BeautifulSoup
import time
from loguru import logger
import json


def show_best_sellers():
    driver = webdriver.Chrome()# Driver do google chrome
    time.sleep(6)

    driver.get("https://www.amazon.com.br/gp/bestsellers/?ref_=nav_cs_bestsellers") # Link da página dos mais vendidos

    html_amz_bestSellers = driver.page_source

    if html_amz_bestSellers:
        soup_bestSellers = BeautifulSoup(html_amz_bestSellers, 'html.parser')
        best_sellers_div = soup_bestSellers.find_all("div",class_="a-column a-span12 a-ws-span10 a-span-last a-ws-span-last")
        if not best_sellers_div:
            logger.error("Esse elemento não foi encontrado!!")
        else:
            for best_sel in best_sellers_div:
                logger.success(f'Produto : {best_sel.text.strip()}')
    else:
        logger.error("Ocorreu um erro ao tentar carregar a página HTML")
    

    try:
        question = int(input("Qual categoria dos mais vendidos deseja ver?: "))
        print("="*30+"Algumas das categorias da Amazon"+"="*30)
        print("1- Cozinha")
        print("2- Moda")
        print("3- Livros")
        print("4- Saúde e bem-estar")
        print("5- Móveis")
        print("6- Materias de construção")
        if question == 1:
            driver.get('https://www.amazon.com.br/gp/bestsellers/kitchen/ref=zg_bs_kitchen_sm')

            html_kitchen = driver.page_source
            if html_kitchen:
                soup_kitchen = BeautifulSoup(html_kitchen,'html.parser')
                best_sel_kitchen = soup_kitchen.find_all('div',class_='a-column a-span12 a-ws-span10 a-span-last a-ws-span-last')
                for kitchen in best_sel_kitchen:
                    logger.success(f'Item de cozinha: {kitchen}')
            else:
                logger.error("Erro ao retornar os itens de cozinha, pois eles não foram encontrados!!")
        elif question == 2:
            driver.get("https://www.amazon.com.br/gp/bestsellers/fashion/ref=zg_bs_nav_fashion_0")

            html_mode = driver.page_source
            if html_mode:
                soup_mode = BeautifulSoup(html_mode,'html.parser')
                best_sel_mode = soup_mode.find_all('div',id='CardInstancen1UrAC_a3Yzqgid9-OgcOQ')
                for mode in best_sel_mode:
                    logger.success(mode.text)
    except Exception as error:
        logger.error(f"Não foi possivel achar a categoria informada: {error}")

def collect_productsJson_info():
    with open('products.json','r') as json_file:
        prod_json = json_file.read()
        print(prod_json)

def suggest_a_product():
    # Dicionário que interagem com o arquivo "products.json"
    products_suggested = {}
    try:
        try:
            with open("products.json",'r',encoding='utf-8') as json_file:
              arr_products_sugg = json.load(json_file)
        except FileNotFoundError:
            arr_products_sugg = []

        name_p = str(input("Qual o nome do produto que você deseja adicionar?: "))
        price_p = float(input("Qual o preço do produto?: "))
        img_p = str(input("Qual a imagem do produto?: "))
        products_suggested['nome'] = name_p
        products_suggested['preco'] = price_p
        products_suggested['img'] = img_p
        arr_products_sugg.append(products_suggested)

        with open('products.json','a+',encoding='utf-8') as products:
            json.dump(products_suggested, products, indent=4,ensure_ascii=False)
        logger.success("produto adicionado no json com sucesso!!")
        print(f"Os produtos que sugeri para serem adicionados: {arr_products_sugg}")
    except Exception as erro:
        logger.error(f"Ocorreu um erro durante a inserção desse produto: {erro}")
    

def ranking_products():
    type_rank = str(input("Por qual tipo de rank deseja?: ")).lower()
    if type_rank == 'categoria':
        mode_cate = "" 
    elif type_rank == "preco":
            pass
    elif type_rank == 'alfabeto':
        pass

def main():
    while True:
        print("0- Encerrar")
        print("1- Ver os mais vendidos")
        print("2- Ver os produtos do arquivo JSON")
        print("3- Inserir outro produtos no JSON")
        print('4- Rankear os produtos')
        question = int(input("Qual operação deseja?: "))
        if question == 1:
            show_best_sellers()
        elif question == 2:
            collect_productsJson_info()
        elif question == 3:
            suggest_a_product()
        elif question == 4:
            ranking_products()
        elif question == 0:
            break



if __name__ == '__main__':
    main()

