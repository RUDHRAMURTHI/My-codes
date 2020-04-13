class rud_drlaptop:  # main class named DrLaptop
    data_customer_rep = {'sudha': 'sudha@1'}  # dictionary for customer representive ----- Use this as credentials for the first time
    data_hardware_eng = {'sahadevan': 'saha@1'}  # dictionary for hardwork engineer ----- Use this as credentials for the first time
    data_admin = {'rudhra': 'rudhra15'}  # dictionary for admin ----- Use this as credentials for the first time
    data_customer = {}# dictionary for customer
    data_assaignment={'sahadevan':[]}#dictinary for assigining hareware engineer:complints
    data_complaints_hardware={}#dictionary for assigining complait:hardware engineer
    data_status={}#dictionary for checking status
    hardware_eng=['sahadevan']
    coustomer_rep=["sudha"]
    All_complaints=[]
    count=100
    def admin(self):#admin module`
        try:
            admin_name = input("\nEnter The Admin UserName:\n ")
            admin_pwd = input("\nEnter The Password:\n ")
            if (admin_pwd == rud_drlaptop.data_admin[admin_name]):#admin authentication

                print("\nWELCOME", admin_name)

                print("\n\n1.ADD CUSTOMER REPRESENTATIVE \n2.ADD HARDWARE ENGINEER \n3.REMOVE CUSTOMER REPRESENTATIVE\n4.REMOVE HARDWARE ENGINEER\n5.EMPLOYEE DETAILS\n6.CHANGE PASSWORD\n7.EXIT")
                n=True
                m=True
                while(n==True or m==True):
                    rud_choise = input("\nEnter The Option Number:\n")
                    try:
                        a=int(rud_choise)
                        if(a>0 and a<8):
                            m=False
                        else:
                            print("\nEnter Valid Option Only\n")
                            m=True
                    except ValueError:
                        m=False
                    n=rud_drlaptop.int_check(self,rud_choise)
                rud_choise=int(rud_choise)
                while (rud_choise < 7 and rud_choise>0):
                    if (rud_choise == 1):#adding customer representative
                        print("\t\t\tADDING CUSTOMER REPRESENTATIVE\n\n")
                        n=True
                        c=True
                        while(n==True or c==True):
                            a = input("\nEnter Executive name:\n")
                            if ((a in rud_drlaptop.coustomer_rep) or (a in rud_drlaptop.hardware_eng)):
                                print("\nThis Username Is Already Present Try New\n")
                                c=True
                            else:
                                c=False
                            n=rud_drlaptop.char_check(self,a)
                        m=True
                        while( m==True):
                            b = input("\nEnter The Password:\n")
                            l=len(b)
                            if(l>=6 and l<=8):
                                m=False
                            else:
                                print("\nTHe Length Of Password Is MIN 6 And MAX 8\n")
                                m=True
                        rud_drlaptop.data_customer_rep[a] = b
                        rud_drlaptop.coustomer_rep.append(a)
                        print("\n\t\t\tThe New CR Details Has Been Updated\n")
                    elif (rud_choise == 2):#adding hardware engineer
                        print("\n\t\t\tADDING HARDWARE ENGINEER\n\n")
                        n = True
                        c=True
                        while (n == True or c==True):
                            a = input("\nEnter Executive Name:\n")
                            if ((a in rud_drlaptop.hardware_eng) or (a in rud_drlaptop.coustomer_rep)):
                                print("\nThis Username Is Already Present pls Enter New\n")
                                c=True
                            else:
                                c=False
                            n = rud_drlaptop.char_check(self, a)
                        m = True
                        while (m == True):
                            b = input("\nEnter The Password:\n")
                            l = len(b)
                            if (l >= 6 and l <= 8):
                                m = False
                            else:
                                print("THe Lenth Of Password Is MIN 6 and MAX 8")####################################
                                m = True
                        rud_drlaptop.data_hardware_eng[a] = b
                        rud_drlaptop.hardware_eng.append(a)
                        rud_drlaptop.data_assaignment[a]=[]
                        print("\n\t\t\tNew HE Details Has Been Updated\n")
                    elif(rud_choise==3):#removing coustomer rep
                        if(rud_drlaptop.coustomer_rep !=[]):
                            print("\n\t\t\tREMOVING CUSTOMER REPRESENTATIVE\n\n")
                            print("\nAvailabe CR:\n",rud_drlaptop.coustomer_rep)
                            n=True
                            while(n==True):
                                a=input("\nChoose Any Customer Rep To Remove:\n")
                                if(a in rud_drlaptop.coustomer_rep):
                                    n=False
                                else:
                                    print("\nChoose CR Displayed Above:\n")
                                    n=True
                            del rud_drlaptop.data_customer_rep[a]
                            rud_drlaptop.coustomer_rep.remove(a)
                            print("\n\t\t\tCR Removed Sucessfully!!!!!!\n")
                        else:
                            print("\n\t\t\tNO CR AVAILABLE PLS ADD CR FIRST!!!\n")
                    elif(rud_choise==4):#removing hardware engineer
                        if(rud_drlaptop.hardware_eng !=[]):
                            print("\n\t\t\tREMOVING HARDWARE ENGINEER\n\n")
                            print("\nAvailable HE:\n",rud_drlaptop.hardware_eng)
                            n = True
                            while (n == True):
                                a = input("Choose Any Hardware Engineer To Remove:\n")
                                if (a in rud_drlaptop.hardware_eng):
                                    n = False
                                else:
                                    print("\nChoose HE Displayed Above\n")
                                    n = True
                            if(rud_drlaptop.data_assaignment[a] !=[]):
                                r=rud_drlaptop.data_assaignment[a]
                                for i in r:
                                    if(rud_drlaptop.data_status[i] != "delivered"):
                                        rud_drlaptop.data_status[i]="reassign"
                            del rud_drlaptop.data_hardware_eng[a]
                            rud_drlaptop.hardware_eng.remove(a)
                            del rud_drlaptop.data_assaignment[a]
                            print("\n\t\t\t HE is Removed Sucessfully!!!!!\n")
                        else:
                            print("\nNO HE AVAILABLE PLS ADD CR FIRST\n")
                    elif(rud_choise==5):#display employee's working
                        print("\n\t\t\tEMPLOYEE DETAILS\n\n")
                        print("\nThe CR's:{username:password}\n")
                        for (k,v) in rud_drlaptop.data_customer_rep.items():
                            print(k,":",v)
                        print("\nThe HE's:{username:password}\n")
                        for (k,v) in rud_drlaptop.data_hardware_eng.items():
                            print(k,":",v)
                    else:
                        print("\n\t\t\tCHANGING PASSWORD\n")
                        while True:
                            while True:
                                a = input("\nEnter Current Password:\n")
                                if (a == admin_pwd):
                                    break
                                else:
                                    print("\nYour current Password is Wrong Pls Try Again\n")
                            m = True
                            while (m == True):
                                b = input("\nEnter The New Password:\n")
                                l = len(b)
                                if (l >= 6 and l <= 8):
                                    m = False
                                else:
                                    print("\nTHe Length Of Password Is MIN 6 And MAX 8\n")
                                    m = True
                            c = input("\nReenter New password:\n")
                            if ((b == c) and (a != b)):
                                print("\nNew Password Has been Updated\n")
                                rud_drlaptop.data_admin[admin_name] = b
                                break
                            else:
                                if (b != c):
                                    print("\nEntered password and Reenterd password Dosen't Match\n")
                                if (a == b):
                                    print("\nYour Current Password And New Password Should not be Same\n")
                    print("\n\n1.ADD CUSTOMER REPRESENTATIVE\n2.ADD HARDWARE ENGINEER \n3.REMOVE CUSTOMER REPRESENTATIVE\n4.REMOVE HARDWARE ENGINEER\n5.EMPLOYEE DETAILS\n6.CHANGE PASSWORD\n7.EXIT")
                    n = True
                    m = True
                    while (n == True or m == True):
                        rud_choise = input("\nEnter The Option Number:\n")
                        try:
                            a = int(rud_choise)
                            if (a > 0 and a < 8):
                                m = False
                            else:
                                print("\nEnter Valid Option Only\n")
                                m = True
                        except ValueError:
                            m = False
                        n = rud_drlaptop.int_check(self, rud_choise)
                    rud_choise = int(rud_choise)
                print("\n\t\t\t",admin_name, "LOGGED OUT")

            else:
                print("\nWrong Login Credentials Pls Try Again\n")
        except KeyError:
            print("\nLogin Credentials Are Wrong\n")


    def customer_represntative(self):
        try:
            if (rud_drlaptop.data_customer_rep !={}):
                cr_name = input("\nEnter The CR Name:\n")
                cr_pwd = input("\nEnter The Password:\n")
                if cr_pwd == rud_drlaptop.data_customer_rep[cr_name]:
                    print("\nWELCOME", cr_name)
                    print("\n1.TAKE A COMPLAINT\n2.CHECK STATUS\n3.ASSIGNING HARDWARE ENGINEER\n4.CHANGE PASSWORD\n5.EXIT")
                    n=True
                    m=True
                    while(n==True or m==True) :
                        choise =input("\nEnter Choice In No:\n")
                        try:
                            a=int(choise)
                            if(a>0 and a<6):
                                m=False
                            else:
                                print("\nEnter Valid Option Only\n")
                                m=True
                        except ValueError:
                            m=False
                        n=rud_drlaptop.int_check(self,choise)
                    choise=int(choise)
                    while (choise < 5 and choise>0):
                        if (choise == 1):#take complaint
                            print("\n\t\t\tTAKING COMPLAINT\n\n")
                            list_complint = []
                            a = "cuid17-"
                            rud_drlaptop.count = rud_drlaptop.count + 1
                            b = str(rud_drlaptop.count)
                            customer_id = a + b#creating id
                            rud_drlaptop.All_complaints.append(customer_id)
                            print("\nGenerated Customer ID=", customer_id)
                            print("\nEnter Customer Details\n")
                            n=True
                            while(n==True):
                                name = input("Name: ")
                                n=rud_drlaptop.char_check(self,name)
                            list_complint.append(name)
                            n=True
                            m=True
                            while(n==True or m==True):
                                mobile = input("Mobile No:")
                                a=len(mobile)
                                if(a==10):
                                    m=False
                                else:
                                    print("\nMobile No Should Equal To 10 Digits\n")
                                    m=True
                                n=rud_drlaptop.int_check(self,mobile)
                            list_complint.append(mobile)
                            n=True
                            while(n==True):
                                lapname = input('Lap Name:')
                                n=rud_drlaptop.char_check(self,lapname)
                            list_complint.append(lapname)
                            n=True
                            while(n==True):
                                lapid = input("Lapid:")
                                l=len(lapid)
                                if(l==6):
                                    n=False
                                else:
                                    print("\nLapid Should Exactly Be 6 Digit:\n")
                                    n=True
                            list_complint.append(lapid)
                            issue = input("Complaint:")
                            list_complint.append(issue)##############
                            rud_drlaptop.data_customer[customer_id] =list_complint
                            print("\nThe Customer Details Are :\n{customerID:[name,mobile no,lapname,lapID,complaint]}\n")
                            for (k,v) in rud_drlaptop.data_customer.items():
                                print(k,":",v)
                            status="complaint registerd"
                            rud_drlaptop.data_status[customer_id]=status
                            print("\nThe Complaint Status Are:\n")
                            for (k,v) in rud_drlaptop.data_status.items():
                                print(k,":",v)
                            print("\nTo Assign Hardware Engineer:\n1.YES--1\n2.NO--2\n")
                            n=True
                            m=True
                            while(n==True or m==True):
                                c=input('\nEnter The Choice:\n')
                                try:
                                    a=int(c)
                                    if(a>0 and a<3):
                                        m=False
                                    else:
                                        print("\nEnter Valid Option Only\n")
                                        m=True
                                except ValueError:
                                    m=False
                                n=rud_drlaptop.int_check(self,c)
                            c=int(c)
                            if(c==1):
                                rud_drlaptop.hardware_eng_assign(self)
                            else:
                                print("\nAssign Complaint Later\n")

                        elif(choise==2): #checking status of complaint
                            print("\n\t\t\tCHECKING COMPLAINT STATUS\n\n")
                            rud_drlaptop.Customer_Check(self)
                        elif(choise==3):#assigning to hardware engineer
                            print("\n\t\t\tASSIGNING TO HARDWARE ENGINEER\n\n")
                            if (rud_drlaptop.data_customer!={}):
                                rud_drlaptop.hardware_eng_assign(self)
                            else:
                                print('\nNO COMPLAINTS REGISTERED YET \n')
                        else:
                            while True:
                                while True:
                                    a=input("\nEnter Current Password:\n")
                                    if(a==cr_pwd):
                                        break
                                    else:
                                        print("\nYour current Password is Wrong Pls Try Again\n")
                                m = True
                                while (m == True):
                                    b = input("\nEnter The New Password:\n")
                                    l = len(b)
                                    if (l >= 6 and l <= 8):
                                        m = False
                                    else:
                                        print("\nTHe Length Of Password Is MIN 6 And MAX 8\n")
                                        m = True
                                c=input("\nReenter New password:\n")
                                if((b==c) and (a!=b)):
                                    print("\nNew Password Has been Updated\n")
                                    rud_drlaptop.data_customer_rep[cr_name]=b
                                    break
                                else:
                                    if(b!=c):
                                        print("\nEntered Password And Reenterd password Dosen't Match\n")
                                    if(a==b):
                                        print("\nYour Current Password And New Password Should Not Be Same\n")

                        print("\n1.TAKE A COMPLAINT\n2.CHECK STATUS\n3.ASSIGNING HARDWARE ENGINEER\n4.CHANGE PASSWORD\n5.EXIT")
                        n = True
                        m = True
                        while (n == True or m == True):
                            choise = input("\nEnter Choice In No:\n")
                            try:
                                a = int(choise)
                                if (a > 0 and a < 6):
                                    m = False
                                else:
                                    print("\n Enter Valid Option Only\n")
                                    m = True
                            except ValueError:
                                m = False
                            n = rud_drlaptop.int_check(self, choise)
                        choise = int(choise)
                    print("\n\t\t\t", cr_name, "Sucssesfully Logged Out\n")

                else:
                    print("\nWrong Login Credentials Pls Try Again\n")
            else:
                print("\nNO CUSTOMER REP IN DR-LAPTOPS S0 RECRUIT CR'S\n")
        except KeyError:
            print("\nLogin Credentials Are Wrong\n")
    def hardware_engineer(self):
        try:
            if (rud_drlaptop.data_hardware_eng !={}):
                he_name=input("\nEnter The HE Name:\n")
                he_pwd=input("\nEnter The Password:\n")
                if he_pwd == rud_drlaptop.data_hardware_eng[he_name]:
                    print("\nWELCOME",he_name)
                    print("\n\n1.CHECK COMPLAINTS ASSIGNIED\n2.UPDATE COMPLAINT STATUS\n3.CHANGE PASSWORD\n4.EXIT")
                    n=True
                    m=True
                    while(n==True or m==True):
                        rudchoise=input("\nEnter The Option No:\n")
                        try:
                            a=int(rudchoise)
                            if(a>0 and a<5):
                                m=False
                            else:
                                print("\nEnter Valid Option Only\n")
                                m=True
                        except ValueError:
                            m=False
                        n=rud_drlaptop.int_check(self,rudchoise)
                    rudchoise=int(rudchoise)
                    while (rudchoise<4 and rudchoise>0):##do this to all while loops
                        if(rudchoise==1):
                            print("\n\t\t\tCHECKING COMPLAINTS ASSIGNED\n\n")
                            if (rud_drlaptop.data_assaignment!={}):
                                if(rud_drlaptop.data_assaignment[he_name]!=[]):
                                    print("\nThe Complaints Assaigned To You Is:\n",rud_drlaptop.data_assaignment[he_name])
                                    n=True
                                    while(n==True):
                                        a=input("\n\nEnter The Complaint ID To See The Details:\n ")
                                        if(a in rud_drlaptop.data_assaignment[he_name]):
                                            n=False
                                        else:
                                            print("\nEnter Only The Complaint ID Shown Above:\n")
                                            n=True
                                    print("\nThe Complaint Details Are:\n [Name,Mobile No,Lapname,Lapid,Complaint]\n",rud_drlaptop.data_customer[a])
                                else:
                                    print("\nNO COMPLAINT ASSIGNED TO YOU\n")
                            else:
                                print("\nNO COMPLAINTS ARE ASSIGNED YET\n")
                        elif(rudchoise==2):
                            print("\n\t\t\tUPDATING STATUS\n\n")
                            if (rud_drlaptop.data_assaignment!={}):
                                if(rud_drlaptop.data_assaignment[he_name]!=[]):
                                    com=rud_drlaptop.data_assaignment[he_name]
                                    print("\nThe ComplaintIDs Assignd To You Is:\n",com)
                                    print('\nThe Status Of The Complaints Shown To Customer Is:\n')
                                    for i in com:
                                        print(i,'=',rud_drlaptop.data_status[i])
                                    n=True
                                    while(n==True):
                                        id=input("\nEnter The Complaint ID Want To Update:")#checking for valid complaint id
                                        if (id in com):
                                            n=False
                                        else:
                                            print("\nEnter Valid Complaint ID Shown Above\n")
                                            n=True
                                    print("\nMAKE YOUR CHOICE FOR UPDATING STATUS:\n\n1.Processing\n2.On Diognising\n3.Delivered(Closing Complaint)\n4.FOR MANUAL UPDATION\n5.For No Change And Deliverd Complaints\n6.Exit")
                                    n=True
                                    m=True
                                    while(n==True or m==True):
                                        u=input("\nEnter The Status Option:\n")#checking for valid option
                                        try:
                                            a=int(u)
                                            if(a>0 and a<7):
                                                m=False
                                            else:
                                                print("\nEnter Valid Option Only\n")
                                                m=True
                                        except ValueError:
                                            m=False
                                        n=rud_drlaptop.int_check(self,u)
                                    u=int(u)
                                    if(u==1):
                                        rud_drlaptop.data_status[id]="Processing"
                                        print("\nStatus Has Been Updated Succesfully\n")
                                    elif(u==2):
                                        rud_drlaptop.data_status[id]="On Diognising"
                                        print("\nStatus Has Been Updated Succesfully\n")
                                    elif (u == 3):
                                        rud_drlaptop.data_status[id] = "delivered"
                                        print("\nStatus Has Been Updated Succesfully\n")
                                    elif(u==4):
                                        print("\nType The Status That You Want To Update Manually\n")
                                        s=input("status:")#do exepthion here atlast
                                        status=" "+s
                                        rud_drlaptop.data_status[id]= status
                                        print("\nStatus Has Been Updated Succesfully\n")
                                    else:
                                        print("\nNO CHANGE IN STATUS\n")
                                else:
                                    print("\nNO COMPLAINTS IS ASSIGNED TO YOU\n")
                            else:
                                print('\nNO COMPLAINTS ARE ASSIGNED YET\n')
                        else:
                            print("\n\t\t\tCHANGING PASSWORD\n")
                            while True:
                                while True:
                                    a = input("\nEnter Current Password:\n")
                                    if (a == he_pwd):
                                        break
                                    else:
                                        print("\nYour current Password is Wrong Pls Try Again\n")
                                m = True
                                while (m == True):
                                    b = input("\nEnter The New Password:\n")
                                    l = len(b)
                                    if (l >= 6 and l <= 8):
                                        m = False
                                    else:
                                        print("\nTHe Length Of Password Is MIN 6 And MAX 8\n")
                                        m = True
                                c = input("\nReenter New password:\n")
                                if ((b == c) and (a != b)):
                                    print("\nNew Password Has been Updated\n")
                                    rud_drlaptop.data_hardware_eng[he_name] = b
                                    break
                                else:
                                    if (b != c):
                                        print("\nEntered password and Reenterd password Dosen't Match\n")
                                    if (a == b):
                                        print("Your Current Password And New Password Should not be Same\n")
                        print("\n\n1.CHECK COMPLAINTS ASSIGNIED\n2.UPDATE COMPLAINT STATUS\n3.CHANGE PASSWORD\n4.EXIT")
                        n = True
                        m = True
                        while (n == True or m == True):
                            rudchoise = input("\nEnter The Option No:\n")
                            try:
                                a = int(rudchoise)
                                if (a > 0 and a < 5):
                                    m = False
                                else:
                                    print("\nEnter Valid Option Only\n")
                                    m = True
                            except ValueError:
                                m = False
                            n = rud_drlaptop.int_check(self, rudchoise)
                        rudchoise = int(rudchoise)
                    print("\n\t\t\t",he_name,"Successfully Logged out\n")
                else:
                    print("\nWrong Login Credentials Pls Try Again\n")
            else:
                print("\nNO HARDWARE ENGINEER IN DR-LAPTOPS SO RECRUIT HE'S\n")
        except KeyError:
            print("\nLogin Credentials Are Wrong\n")
    def hardware_eng_assign(self):
        if(rud_drlaptop.data_hardware_eng !={}):
            print("\nThe Available Customer Complaints Are:\n\ncomplaintID:[name,mobile no,lapname,lapid,complaint]:")
            for (k,v) in rud_drlaptop.data_customer.items():
                print(k,":",v)
            print('\nThe Available Hardware Engineers are:\n', rud_drlaptop.hardware_eng)
            print("\nStatus Of All Complaints:")
            for (a,b) in rud_drlaptop.data_status.items():
                print(a, ":", b)
            n = True
            while (n == True):
                cus = input('\nChoose The Complaint ID Want To Assaign:')
                if (cus in rud_drlaptop.All_complaints):
                    n = False
                else:
                    print("\nEnter Only The Correct Complaint ID Shown Above")
                    n = True
            if ((rud_drlaptop.data_status[cus] == "complaint registerd") or (rud_drlaptop.data_status[cus] == "reassign")):
                n = True
                while (n == True):
                    h = input('\nChoose The Hardware Engineer Name Want To Assagin:\n')
                    if (h in rud_drlaptop.hardware_eng):
                        n = False
                    else:
                        print("\nEnter Only The Hardware Engineers Displayed Above:")
                        n = True
                if (rud_drlaptop.data_assaignment[h] == []):
                    list_hardware = []
                else:
                    list_hardware = rud_drlaptop.data_assaignment[h]

                list_hardware.append(cus)
                rud_drlaptop.data_assaignment[h] = list_hardware
                rud_drlaptop.data_complaints_hardware[cus] = h
                rud_drlaptop.data_status[cus] = " Assaigned to Hardware Hngineer"
                print("\nThe Complaint Has Been Assagined To HE\n")
            else:
                print("\nThe Complaint Is Already Assigned To A Hardware Engineer\n")
            print("\nThe Status of Complaints Is:\n",rud_drlaptop.data_status[cus])
            print("\nThe Complaint Is Assigned To:\n",rud_drlaptop.data_complaints_hardware[cus])
        else:
            print("\nNO HARDWARE ENGINEERS PRESENT PLS ADD THEM FIRST\n")
    def Customer_Check(self):
        if (rud_drlaptop.data_customer != {}):
            n = True
            while (n == True):
                com_id = input("\nEnter The Customer_ID:\n")  # coustomer id
                if (com_id in rud_drlaptop.All_complaints):
                    n = False
                else:
                    print("\nEnter Valid Cusromer ID\n")
                    n = True
            i = rud_drlaptop.data_status[com_id]
            print("\nThe Customer Status is:\n", i)
            print('\nThe Customer Detail Is:\n[name,mobile no,lapname,lapid,complaint]\n',rud_drlaptop.data_customer[com_id])
            try:
                if (rud_drlaptop.data_complaints_hardware != {}):
                    print('\nThe Complaint Is Assigned To:', rud_drlaptop.data_complaints_hardware[com_id])
                else:
                    print("\nNo Complaints Are Assigned To Hardware Engineer Yet\n")
            except KeyError:
                print("\nThis Complaint Is Not Yet Assigned To HE Yet\n")
        else:
            print("\nNo Complaint Registered Yet \n")

    def int_check(self,x):
        n = x.isdigit()
        if (n == True):
            return (False)
        else:
            print('\nEnter Appropriate Integer Only\n')
            return (True)

    def char_check(self,x):
        n = x.isalpha()
        if (n == True):
            return (False)
        else:
            print("\nEnter Charaters Only\n")
            return (True)

d = rud_drlaptop()
while True:
    print("\n\n\t\t\t$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$!!!!!!!WELCOME TO DR-LAPTOPS!!!!!!$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("\n\n\n\nChoose The Number For Login\n\n1.Admin\n2.CUSTOMER REPRESENTATIVE\n3.HARDWARE ENGINEER\n4.CUSTOMER TRACKING\n5.EXIT")
    n = True
    m = True
    while (n == True or m == True):
        a = input("\nEnter The Option No:\n")
        try:
            b = int(a)
            if (b > 0 and b < 6):
                m = False
            else:
                print("\nENTER VALID OPTION ONLY\n")
                m = True
        except ValueError:
            m = False
        n = d.int_check(a)
    a = int(a)
    if(a==1):
        print("\n\n\n*******************************************ADMIN PORTAL!!!!!*******************************************\n\n\n")
        d.admin()
    elif (a == 2):
        print("\n\n\n****************************************CUSTOMER REPRESENTATIVE PORTAL!!!!**********************************\n\n\n")
        d.customer_represntative()
    elif(a==3):
        print("\n\n\n**************************************HARDWARE ENGINEER PORTAL!!!!!!*****************************************\n\n\n")
        d.hardware_engineer()
    elif(a==4):
        print("\n\n\n***********************************************CUSTOMER PORTAL!!!!!!!******************************************\n\n\n")
        d.Customer_Check()
    elif(a==5):
        print("\n\n\n*******************************************Visit DR-Laptops Again*******************************************\n\n\n")
        break
    else:
        print("\nEnter Correct Option\nPls Try Again\n")
