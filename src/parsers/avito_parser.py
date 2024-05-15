import json

def parse_avito_apartments(driver, By):
    
    data = {"oneBedroom": []}
    
    for page in range(1):
        url = f"https://www.avito.ru/kaliningrad/kvartiry/sdam/na_dlitelnyy_srok-ASgBAgICAkSSA8gQ8AeQUg?context=H4sIAAAAAAAA_0q0MrSqLraysFJKK8rPDUhMT1WyLrYyNLNSKk5NLErOcMsvyg3PTElPLVGyrgUEAAD__xf8iH4tAAAA&p={page}"
        driver.get(url)

        element = driver.find_element(
            By.CSS_SELECTOR, '[data-marker="catalog-serp"]')
        carts = element.find_elements(By.CSS_SELECTOR, '[data-marker="item"]')

        for cart in carts:
            item_id = cart.get_attribute('data-item-id')
            title = cart.find_element(
                By.CSS_SELECTOR, '[data-marker="item-title"]')
            price = cart.find_element(
                By.CSS_SELECTOR, '[data-marker="item-price"]')
            pledge = cart.find_element(
                By.CSS_SELECTOR, '[data-marker="item-specific-params"]')
            
            address_ful = cart.find_element(By.CSS_SELECTOR, '[data-marker="item-address"]')
            
            street = address_ful.get_attribute("textContent")
            
            
            link = cart.find_element(By.CSS_SELECTOR, '[data-marker="item-title"]')
            url_link = link.get_attribute("href")
            
            xpath_path = '/html/body/div[1]/div/div[3]/div/div[2]/div[3]/div[3]/div[4]/div[2]/div[1]/div/div/div[1]/a/div/div/ul/li/div/img'
            
            item_photo = cart.find_element(By.CSS_SELECTOR, '[data-marker="item-photo"]')
            image = item_photo.find_element(By.XPATH, xpath_path)
            image_url = image.get_attribute('src')
            
            data["oneBedroom"].append({
                'id': item_id,
                'title': title.text,
                'price': price.text,
                'pledge': pledge.text,
                'street': street,
                'url': { 
                    'url_link': url_link,
                    'image_URl': image_url
                }
            })
    
    
    with open('avito_apartments.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print("Данные успешно записаны в файл avito_apartments.json")
    print("Все готово!")
