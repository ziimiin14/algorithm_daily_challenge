class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_email = set()
        for email in emails:
            find_At = email.find('@')
            length = len(email)
            # find_Plus = email.find('+')
            if find_At != -1:
                front = ''
                back = email[find_At+1:]
                
                for i in range(0,find_At):
                    if email[i] == '+':
                        break
                    elif email[i] == '.':
                        continue
                    else:
                        front += email[i]
                
                full_email = front+'@'+back
                if full_email[-4:] == '.com':
                    unique_email.add(full_email)
                
        return len(unique_email)
                
