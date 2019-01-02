class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        local_name_dict = {}
        for s in emails:
            name = s.split('@')
            local_name = name[0]
            domain_name = name[1]
            #去掉 + 之后的内容
            local_name = local_name.split('+')[0]
            #去掉 .
            local_name = "".join(local_name.split('.'))
            if local_name+domain_name not in local_name_dict:
                local_name_dict.update({local_name+domain_name:1})
        return len(local_name_dict)

#===========================
s = Solution()
s.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"])

