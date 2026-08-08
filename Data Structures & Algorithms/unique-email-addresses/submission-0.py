class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        counter = 0
        emailSet = set()
        for i in range(len(emails)):
            l = len(emails[i])
            atSymbol = emails[i].find('@')
            
            local = emails[i][0:atSymbol]
            domain = emails[i][atSymbol+1:l]
            
            #local
            local = local.replace(".","")
            
            #print(local[0:localP] + " or "+ local)
            if local.find('+') != -1:
                localP = local.find('+')
                local = local[0:localP]
            #if local[0:localP] != local:
               
            #counter += 1
            print(local)
            emailSet.add(local+domain)
            #domain
        print(emailSet)
        return len(emailSet)