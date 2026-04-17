from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
from loguru import logger
import json
import pyautogui as pya
import pyperclip as pyp

def show_best_sellers():
    driver = webdriver.Chrome()# Driver do google chrome
    time.sleep(6)

    driver.get("https://www.amazon.com.br/gp/bestsellers/?ref_=navm_cs_bestsellers") # Link da página dos mais vendidos

    html_amz_bestSellers = driver.page_source

    if html_amz_bestSellers:
        best_sellers_menu = driver.find_element(By.ID,"zg-right-col")
        time.sleep(5)
        if not best_sellers_menu:
            logger.error("Esse elemento não foi encontrado!!")
        else:
            logger.success(f'Produtos : {best_sellers_menu.text.strip()}')
    else:
        logger.error("Ocorreu um erro ao tentar carregar a página HTML")
    

    try:
        print("="*30+"Algumas das categorias da Amazon"+"="*30)
        print("1- Cozinha")
        print("2- Moda")
        print("3- Livros")
        print("4- Saúde e bem-estar")
        print("5- Móveis")
        print("6- Materias de construção")
        question = int(input("Qual categoria dos mais vendidos deseja ver?: "))
        if question == 1:
            driver.get('https://www.amazon.com.br/gp/bestsellers/kitchen/ref=zg_bs_nav_kitchen_0')

            html_kitchen = driver.page_source
            if html_kitchen:
                soup_kitchen = BeautifulSoup(html_kitchen,'html.parser')
                best_sel_kitchen = soup_kitchen.find_all('div',class_='_cDEzb_p13n-sc-css-line-clamp-3_g3dy1')
                for kitchen in best_sel_kitchen:
                    logger.success(f'Item de cozinha: {kitchen.text + '\n'}\n')
            else:
                logger.error("Erro ao retornar os itens de cozinha, pois eles não foram encontrados!!")
        elif question == 2:
            driver.get("https://www.amazon.com.br/gp/bestsellers/fashion/ref=zg_bs_nav_fashion_0")

            html_mode = driver.page_source
            if html_mode:
                soup_mode = BeautifulSoup(html_mode,'html.parser')
                best_sel_mode = soup_mode.find_all('div',class_='_cDEzb_p13n-sc-css-line-clamp-3_g3dy1')
                for mode in best_sel_mode:
                    logger.success(f'Item de moda: {mode.text}')

        elif question == 3:
            driver.get("https://www.amazon.com.br/gp/bestsellers/books/ref=zg_bs_nav_books_0")

            html_books = driver.page_source
            if html_books:
                soup_books = BeautifulSoup(html_books,'html.parser')
                best_sel_books = soup_books.find_all("ol",class_="_cDEzb_p13n-sc-css-line-clamp-3_g3dy1")
                for book in best_sel_books:
                    logger.success(book.text)
        elif question == 4:
            driver.get("https://www.amazon.com.br/gp/bestsellers/hpc/ref=zg_bs_nav_hpc_0")

            html_health = driver.page_source
            if html_health:
                soup_health = BeautifulSoup(html_books,"html.parser")
                best_sel_health = soup_health.find_all('div',class_='_cDEzb_p13n-sc-css-line-clamp-3_g3dy1')
                for health in best_sel_health:
                    logger.success(health.text)

    except Exception as error:
        logger.error(f"Não foi possivel achar a categoria informada: {error}")

def collect_productsJson_info():
    with open('products.json','r') as json_file:
        prod_json = json_file.read()
        print(prod_json)

def suggest_a_product():
    # Dicionário que interage com o arquivo "products.json"
    products_suggested = {}
    try:
        try:
            with open("products.json",'r',encoding='utf-8') as json_file:
              arr_products_sugg = json.load(json_file)
        except FileNotFoundError:
            logger.error("Arquivo json não encontrado!!")
        
        name_p = str(input("Qual o nome do produto que você deseja adicionar?: "))
        price_p = float(input("Qual o preço do produto?: "))
        img_p = str(input("Qual a imagem do produto?: "))

        arr_products_sugg
        arr_products_sugg[name_p] = {'preco':price_p,'img':img_p}

        with open('products.json','w',encoding='utf-8') as products:
            products_suggested = json.dump(arr_products_sugg, products, indent=4,ensure_ascii=False)
            logger.success(f"Lista de produtos no JSON: {products_suggested}")
        logger.success("produto adicionado no json com sucesso!!")
    except Exception as erro:
        logger.error(f"Ocorreu um erro durante a inserção desse produto: {erro}")
    

def ranking_products():
    driver = webdriver.Chrome()
    type_rank = str(input("Por qual tipo de rank deseja?: ")).lower()
    if type_rank == 'categoria':
        driver.get("https://www.amazon.com.br/gp/bestsellers/?ref_=nav_cs_bestsellers")

        html_category = driver.page_source
        if html_category:
            list_categories = driver.find_element(By.CSS_SELECTOR,"ul._p13n-zg-nav-tree-all_style_zg-browse-group__88fbz")
            time.sleep(5)
            logger.success(f"\n Categorias : \n{list_categories.text}")
            
        driver.quit()

    elif type_rank == "preco":
        driver.get("https://www.amazon.com.br/gp/movers-and-shakers/ref=zg_bs_tab_bsms")
        time.sleep(4)

        html_price = driver.page_source
        soup_price = BeautifulSoup(html_price,'html.parser')

        product_name = soup_price.find_all("div",class_="p13n-sc-truncate-desktop-type2")
        price_rank = soup_price.find_all('div',class_="a-row") and soup_price.find_all('span',class_='_cDEzb_p13n-sc-price_3mJ9Z')
        products_collection = []
        print("*"*30+" 10 produtos mais caros "+"*"*30)
        
        for name, price in zip(product_name, price_rank):
            price_txt = price.text.strip()
            price_txt = price_txt.replace("R$","")
            price_txt = price_txt.replace("\xa0","")
            price_txt = price_txt.replace('.','').replace(",",".")
            txt_clean = price_txt.strip()
            txt_clean_num = float(txt_clean)
            products_collection.append({'produto':name.text,'preço':txt_clean_num})
                   
        order_list = sorted(products_collection,key=lambda x: x['preço'],reverse=True)
        for pric in order_list[:10]:
                logger.success(f"Produto:{pric['produto']}, Preço:{pric['preço']:.2f}")

        driver.quit()
        
    elif type_rank == 'alfabeto':
        driver.get("https://www.amazon.com.br/gp/movers-and-shakers/ref=zg_bsnr_tab_bsms") # Link dos produtos em alta
        html_amazon = driver.page_source
        soup_categories_li = BeautifulSoup(html_amazon,'html.parser')
        categories_li = soup_categories_li.find_all("li",class_="_p13n-zg-nav-tree-all_style_zg-browse-item__1rdKf _p13n-zg-nav-tree-all_style_zg-browse-height-small__nleKL")

        category = str(input("De qual categoria você deseja ver os produtos por ordem alfabética?: "))
        products_order_list = []
       
        if category == 'cozinha':
                    time.sleep(3)
                    driver.get("https://www.amazon.com.br/gp/browse.html?node=16957125011&ref_=nav_em_kitchen_all_0_2_18_2")

                    alpha_rank_kitchen = driver.find_element(By.CSS_SELECTOR,"div.a-section dcl-product-attributes")
                    products_order_list.append(alpha_rank_kitchen.text)
                 
                       
        elif category == 'moda':
                    time.sleep(3)
                    driver.get("https://www.amazon.com.br/gp/bestsellers/fashion/ref=zg_bs_nav_fashion_0")
                    alpha_rank_mode = driver.find_element(By.CLASS_NAME,"_cDEzb_iveVideoWrapper_JJ34T")
                    products_order_list.append(alpha_rank_mode.text)
                    
        elif category =='livros':
                time.sleep(3)
        print(products_order_list.sort())
        print("*"*30+f"Produtos de {category} por ordem alfábetica"+"*"*30)
        alpha_rank_sort = "".join(products_order_list)
        for alpha in alpha_rank_sort:
            logger.success(f"{alpha}")

        driver.quit()

def search_specific_product():
    driver = webdriver.Chrome()
    driver.get("https://www.amazon.com.br/ref=nav_logo")
    product = str(input("Me diga o nome do produto que deseja procurar?: "))
    list_products_search = []
    time.sleep(4)
    pya.moveTo(x=567,y=177)
    time.sleep(3)
    pya.click()
    time.sleep(3)
    pya.write(product)
    time.sleep(3)
    pya.press('enter')
    time.sleep(3)
    pya.moveTo(x=223,y=62)
    time.sleep(2)
    pya.click()
    time.sleep(2)
    driver_url = pyp.paste()
    print(driver_url)
    time.sleep(2)
    driver.get(driver_url)
    div_products = driver.find_element(By.CLASS_NAME,'a-section a-spacing-small puis-padding-left-small puis-padding-right-small')
    list_products_search.append(div_products.text)
    for prod in list_products_search[:10]:
        print(prod)
    print(list_products_search)

def main():
    while True:
        print("0- Encerrar")
        print("1- Ver os mais vendidos")
        print("2- Ver os produtos do arquivo JSON")
        print("3- Inserir outro produtos no JSON")
        print('4- Rankear os produtos')
        print("5- Pesquisar produto específico")
        question = int(input("Qual operação deseja?: "))
        if question == 1:
            show_best_sellers()
        elif question == 2:
            collect_productsJson_info()
        elif question == 3:
            suggest_a_product()
        elif question == 4:
            ranking_products()
        elif question == 5:
            search_specific_product()
        elif question == 0:
            break
        else:
            print("Operação inválda")



if __name__ == '__main__':
    main()

