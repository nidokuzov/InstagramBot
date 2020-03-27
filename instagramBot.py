from selenium import webdriver
from time import sleep
import username
import random 


class instagramBot:
	def __init__(self, username, password, hashtag, comments):
		account = username
		self.driver = webdriver.Chrome()
		self.driver.get("https://www.instagram.com")
		sleep(2)
		self.driver.find_element_by_xpath("//input[@name=\"username\"] ").send_keys(account)
		self.driver.find_element_by_xpath("//input[@name=\"password\"] ").send_keys(password)
		sleep(2)
		self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div").click()
		sleep(5)
		self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]").click()
		self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div/div/span[2]").click()
		self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input").send_keys(hashtag)
		sleep(2)
		self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]/div/div/div[1]/span").click()
		sleep(5)
		self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div/div[2]/div[2]/a").click()
		sleep(2)
		commented = 0
		followed = 0
		liked = 0		
		for x in range(1,10000):
			try:
				if(x % 100 == 0):
					print("checked" + str(x))
				if(random.randrange(5) % 2 == 0):
					sleep(2)
					self.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button").click()
					liked = liked + 1
					print("liked " + str(liked))
					sleep(1)
					if(random.randrange(22) % 21 == 0):
						sleep(3)
						self.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button").click()
						followed = followed + 1
						print("followed " + str(followed))
					if(random.randrange(3) % 2 == 0):
						sleep(5)	
						self.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/textarea").click()
						self.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/textarea").send_keys(comments[random.randrange(len(comments)) - 1])
						self.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/button").click()
						commented = commented + 1
						print("commented " + str(commented))
						sleep(5)
			except Exception as e:
				sleep(3)
				self.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button").click()
			sleep(1)
			self.driver.find_element_by_xpath("/html/body/div[4]/div[1]/div/div/a[2]").click()
			sleep(2)

instagramBot(username.username, username.password, username.hashtag, username.nice_comments)