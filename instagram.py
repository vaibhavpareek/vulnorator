import requests,json,os,terminal_banner,pyfiglet,re
from bs4 import BeautifulSoup
def insta():
	print("\033[1;35;48m")
	print(pyfiglet.figlet_format("Instagram Crawler",font="slant"))
	try:
		link = input("Enter Username of Instagram : ")
		page = requests.get("https://www.instagram.com/"+link+"/")
		soup = BeautifulSoup(page.text,'html.parser')
		all_script = soup.find_all('script')
		json_data = json.loads(all_script[3].text)
		print("\033[1;32;48mName : \033[1;35;48m"+json_data['name']+"\n")
		print("\033[1;32;48mType : \033[1;35;48m"+json_data["@type"]+"\n")
		print("\033[1;32;48mInstagram Id :\033[1;35;48m "+json_data['mainEntityofPage']['@id']+"\n")
		script_tag = soup.find('script', text=re.compile('window\._sharedData'))
		shared_data = script_tag.string.partition('=')[-1].strip(' ;')
		json_value = json.loads(shared_data)
		print("\033[1;32;48mBiography :\033[10;35;48m "+ json_value['entry_data']['ProfilePage'][0]['graphql']['user']['biography']+"\n")
		if(json_value['entry_data']['ProfilePage'][0]['graphql']['user']['is_verified']):
			print("\033[1;32;48mVerified :\033[10;35;48m Yes\n")
		else:
			print("\033[1;32;48mVerified :\033[10;35;48m No\n")
		print("\033[1;32;48mFollowers : \033[1;35;48m" + str(json_value['entry_data']['ProfilePage'][0]['graphql']['user']['edge_followed_by']['count'])+"\n")
		print("\033[1;32;48mFollowing : \033[1;35;48m"+str(json_value['entry_data']['ProfilePage'][0]['graphql']['user']['edge_follow']['count'])+"\n")
		if(json_value['entry_data']['ProfilePage'][0]['graphql']['user']['is_private']==False):
			print("\033[1;32;48mAccount :\033[1;35;48m Public"+"\n")
		else:
			print("\033[1;32;48mAccount :\033[1;35;48m Private"+"\n")
		post = json_value['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['count'];
		print("\033[1;32;48mPosts : \033[1;35;48m"+str(json_value['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['count'])+"\n")
		print("\033[1;32;48mFacebook Page Attached : \033[1;35;48m"+str(json_value['entry_data']['ProfilePage'][0]['graphql']['user']['connected_fb_page'])+"\n")
		os.system("curl '"+json_value['entry_data']['ProfilePage'][0]['graphql']['user']['profile_pic_url']+"' -o 'images/profile.jpg'")
		print("\033[1;33;48mDownloaded Profile Pic saved in folder images"+"\n")
		n = 1
		os.system("mkdir -p OUTPUT/instacrawl/"+link+"/images")
		fp = open("OUTPUT/instacrawl/"+link+"/images/details.txt","w+")
		while(n<=post):
			print("\n\033[1;33;48mDownloading "+str(n)+" Post"+"\n")
			print("\033[1;32;48mCaption "+str(n)+ " : \033[1;34;48m"+json_value['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['edges'][n-1]['node']['edge_media_to_caption']['edges'][0]['node']['text']+"\n")
			fp.write("Caption"+str(n)+ " : "+json_value['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['edges'][n-1]['node']['edge_media_to_caption']['edges'][0]['node']['text']+"\n")
			print("\033[1;32;48mLikes : \033[1;34;48m"+str(json_value['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['edges'][n-1]['node']['edge_liked_by']['count'])+"\n")
			os.system("curl '"+ json_value['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['edges'][n-1]['node']['display_url']+"' --output 'OUTPUT/instacrawl/"+link+"/images/image"+str(n)+".jpg'")	
			n += 1
		fp.close()
		print("Done")
	except :
		print("You must have entered something wrong")
	