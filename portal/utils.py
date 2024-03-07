import requests, bs4
import json
from .models import Category, JobPost
from django.utils.text import slugify

def getCategory(category):
    if category == 'All Organisations':
        return 'Other Jobs'

    elif category == 'Accounting & Finance Jobs' or category=='Accounting' or category=='Auditing': 
        return 'Accounting & Auditing Jobs'

    elif category == 'Admin & Office Jobs' or category == 'Administration' or category=='Secretarial/Receptionist':
        return 'Administrative Jobs'

    elif category == 'Agriculture, Farming Jobs' or category=='Agriculture':
        return 'Farming Jobs'

    elif category == 'Applied Sciences, Aviation Jobs' or category=='Applied' or category=='Biotechnology':
        return 'Medicine & Pharmaceutical Jobs'

    elif category == 'Apprenticeship Intake Jobs' or category=='Apprentice':
        return 'Attachment & Internship Jobs'

    elif category == 'Attachment & Internship Jobs':
        return 'Attachment & Internship Jobs'

    elif category == 'Artisan':
        return 'Art & Design Jobs'

    elif category == 'Arts' or category=='Designer':
        return 'Art & Design Jobs'

    elif category == 'Automotive' or category=='Mechanic':
        return 'Automotive'

    elif category == 'Aviation':
        return 'Other Jobs'

    elif category == 'Banking Jobs':
        return 'Accounting & Auditing Jobs' 

    elif category == 'Business':
        return 'Business'

    elif category == 'College, University & Nursing Intakes' or category=='College' or category=='Education':
        return 'Education & Teaching Jobs'

    elif category == 'Construction Jobs' or category=='Construction':
        return 'Building & Architecture Jobs'

    elif category == 'Consultancy, Research Jobs' or category=='Consultancy' or category=='Customer':
        return 'Customer Service & Support Jobs'

    elif category == 'Cruise Ship & Cabin Crew Jobs':
        return 'Other Jobs'

    elif category == 'Diaspora Jobs' or category=='Development':
        return 'Other Jobs'

    elif category == 'Driving & Logistics Jobs' or category=='Driver' or category=='Transportation':
        return 'Drivers'

    elif category == 'Economics':
        return 'Economics'

    elif category == 'Education & Teaching Jobs':
        return 'Teaching & Training Jobs'

    elif category == 'Engineering Jobs' or category=='Engineering':
        return 'Engineering Jobs'

    elif category == 'Environmental, Forestry Jobs' or category=='Environmental':
        return 'Other Jobs'

    elif category == 'General Work Jobs' or category=='General' or category=='Local':
        return 'Other Jobs'

    elif category == 'Graduate Trainee Jobs' or category=='Graduate':
        return 'Teaching & Training Jobs'

    elif category == 'Government':
        return 'Government'

    elif category == 'Healthcare, Pharmacy, Doctors Jobs' or category=='Healthcare':
        return 'Medicine & Pharmaceutical Jobs'

    elif category == 'Human Resources, HR Jobs' or category=='Human':
        return 'Human Resources, HR Jobs'

    elif category == 'ICT & Computer Jobs' or category=='I.C.T' or category=='Software' or category=='Telecommunications':
        return 'IT & Telecoms Jobs'

    elif category == 'Insurance Jobs' or category=='Finance':
        return 'Banking, Financial, Insurance'

    elif category == 'Legal Jobs' or category=='Law':
        return 'Legal Jobs'

    elif category == 'Library, Records Management Jobs' or category=='Records' or category=='Other':
        return 'Other Jobs'

    elif category == 'Manufacturing Jobs' or category=='Minimal' or category=='Statistics' or category=='Woodwork':
        return 'Other Jobs'

    elif category == 'Media Jobs' or category=='Media':
        return 'Media, PR & Communication Jobs'

    elif category == 'Media, PR & Communication Jobs' or category=='journalism':
        return 'Media, PR & Communication Jobs'


    elif category == 'Mining Jobs' or category=='Mining':
        return 'Mining, Metals, Minerals, Oil'

    elif category == 'NGO & Social Services Jobs' or category=='NGOs' or category=='Voluntary':
        return 'NGO & Social Services Jobs'

    elif category == 'Nursing Jobs':
        return 'Medicine & Pharmaceutical Jobs'

    elif category == 'Procurement, Purchasing Jobs' or category == 'Logistics' or category=='Purchasing' or category=='Quality':
        return 'Supply Chain & Procurement Jobs'

    elif category == 'Project':
        return 'Project Management Jobs'

    elif category == 'Psychology' or category=='Social':
        return 'Social Development Jobs'

    elif category == 'Real Estate Jobs' or category=='Real':
        return 'Consulting & Strategy Jobs'

    elif category == 'Retail Jobs' or category=='Retail/Wholesale' or category=='Risk' or category=='Sales':
        return 'Trades & Services Jobs'

    elif category == 'Sales & Marketing Jobs':
        return 'Marketing & Communications Jobs'

    elif category == 'Scholarships':
        return 'Education & Teaching Jobs'

    elif category == 'Security Jobs' or category=='Security':
        return 'Security Jobs'

    elif category == 'Science':
        return 'Science'

    elif category == 'SHE Jobs':
        return 'SHE Jobs'

    elif category == 'Sports & Recreation Jobs':
        return 'Other Jobs'

    elif category == 'Stores & Warehouse Jobs':
        return 'Trades & Services Jobs'

    elif category == 'Strategic Management Jobs' or category=='Executive' or category=='General':
        return 'Consulting & Strategy Jobs'

    elif category == 'Student Loans' or category=='Internship':
        return 'Attachment & Internship Jobs'

    elif category == 'Tenders':
        return 'Research Jobs'

    elif category == 'Tourism, Hospitality, Hotel Jobs' or category=='Hospitality':
        return 'Tourism, Hospitality, Hotel Jobs'

    else:
        return 'Other Jobs'


def classifieds():
    url = 'https://www.classifieds.co.zw/zimbabwe-jobs'
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, features="html.parser")
    linkElems = soup.select('.sub-category')

    for link in linkElems:
        # title = link.findChildren('a')[0].getText()
        link_url = link.findChildren('a')[0].attrs['href']
        res = requests.get(link_url)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, features="html.parser")
        job_postings = soup.select('.listing-title')
        category = link.getText().strip().split('\n')[0]

        print('>>>')
        print(category)
        print('>>>')

        try:
            Category.objects.get_or_create(name=category, slug=slugify(category))
        except:
            print('*************************************************************')
            print('Some Category Error')
            print('*************************************************************')

        try:
            for job_post in job_postings[:3]:
                
                try:
                    link_to_job = job_post.findChildren('a')[0].attrs['href']
                    res = requests.get(link_to_job)
                    res.raise_for_status()
                    soup = bs4.BeautifulSoup(res.text, features="html.parser")

                    title = soup.select('.page-header')[0].getText()
                    description = soup.select('.listing-description')[0].findChildren('p')[0].getText()
                except:
                    continue

                obj = {
                    'title': title,
                    'link_to_job': link_to_job,
                    'description': description,
                    'category': category
                }

                try:
                    category = Category.objects.get(slug=slugify(obj['category']))
                    JobPost.objects.get_or_create(
                        title = obj['title'],
                        link_to_job = obj['link_to_job'],
                        description = obj['description'],
                        category = category,
                    )
                    print(title)
                except:
                    print('*************************************************************')
                    print('Some Job Post Error')
                    print('*************************************************************')
        except:
            continue
    return
    
def vacancymail():
    url = 'http://vacancymail.co.zw/'
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, features="html.parser")
    linkElems = soup.select('.links')

    categories = []
    jobs = []

    for link in linkElems[:-12]:
        
        if ('(' in link.getText().replace("\n", "" ).strip()):
            category = getCategory(link.getText().replace("\n", "" ).strip()[:-4])
        else:
            category = getCategory(link.getText().replace("\n", "" ).strip())

        try:
            Category.objects.get_or_create(name=category, slug=slugify(category))
        except:
            print('*************************************************************')
            print('Some Category Error')
            print('*************************************************************')

        link_url = url + link.attrs['href']
        res = requests.get(link_url)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, features="html.parser")
        job_list = soup.select(".job-list-item-title")
        print(category)
        
        try:
            for job in job_list[:3]:
                
                try:
                    link_to_job = url + job.findChildren('a')[0].attrs['href']
                    title = job.findChildren('a')[0].findChildren('h1')[0].getText()
                    category = category
                    res = requests.get(link_to_job)
                    res.raise_for_status()
                    soup = bs4.BeautifulSoup(res.text, features="html.parser")

                    description = soup.select("p")[1].findChildren('p')[0].getText()

                except:
                    continue
                
                obj = {
                    'title': title,
                    'category': category,
                    'description': description,
                    'link_to_job': link_to_job
                }

                try:
                    category = Category.objects.get(slug=slugify(obj['category']))
                    post = JobPost.objects.get_or_create(
                        title = obj['title'],
                        link_to_job = obj['link_to_job'],
                        description = obj['description'],
                        category = category,
                    )
                    print(category)
                    print(post)
                except:
                    print('*************************************************************')
                    print('Some Job Post Error')
                    print('*************************************************************')
        except:
            print('continuing')
            continue

    return


def ihararejob():
    base_url = 'https://ihararejobs.com'
    res = requests.get(base_url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, features="html.parser")

    linkElems = soup.select('.cat-item > a')
    for link in linkElems:
        if '(' in link.getText():
            category = getCategory(link.getText().split(' ')[0])
        else:
            category = getCategory(link.getText())

        try:
            Category.objects.get_or_create(name=category, slug=slugify(category))
        except:
            print('*************************************************************')
            print('Some Category Error')
            print('*************************************************************')

        category_url = base_url + link.attrs['href']
        res = requests.get(category_url)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, features="html.parser")

        job_list = soup.select(".listings.job")

        try:
            for job in job_list[:3]:
                try:
                    title = job.findChildren('a')[1].getText().strip()
                    link_to_job = base_url + job.findChildren('a')[1].attrs['href']
                    category = category

                    res = requests.get(link_to_job)
                    res.raise_for_status()
                    soup = bs4.BeautifulSoup(res.text, features="html.parser")

                    try:
                        description = soup.select('.description')[0].findChildren('p')[3].getText()
                    except:
                        description = f'{title} - {category}'

                except:
                    continue

                obj = {
                    'title': title,
                    'category': category,
                    'description': description,
                    'link_to_job': link_to_job
                }
                print(obj)

                try:
                    category = Category.objects.get(slug=slugify(obj['category']))
                    post = JobPost.objects.get_or_create(
                        title = obj['title'],
                        link_to_job = obj['link_to_job'],
                        description = obj['description'],
                        category = category,
                    )
                    print(category)
                    print(post)
                except Exception as e:
                    print('*************************************************************')
                    print(e, '//////')
                    print('*************************************************************')


        except Exception as e: 
            print('*************************************************************')
            print(e)
            print('*************************************************************')



def scrap():
    print('Scraping Classifieds....')
    classifieds()

    print('Scraping VacancyMail...')
    vacancymail()

    print('Scraping iHarare...')
    ihararejob()

    print('Done...')


