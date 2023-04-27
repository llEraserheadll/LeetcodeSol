class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        #creating hash set
        uniqueemails = set() 
        
        for email in emails:
            cleanmail = []
            
            for currChar in email:
                if currChar == '@' or currChar == '+':
                    break
                    
                
                if currChar != '.':
                    cleanmail.append(currChar)
            
            domainname = []
            for currChar in reversed(email):
                domainname.append(currChar)
                
                if currChar == '@':
                    break
                    
            
            domainname = ''.join(domainname[::-1])
            cleanmail = ''.join(cleanmail)
            uniqueemails.add(cleanmail + domainname)
            
        return len(uniqueemails)
        