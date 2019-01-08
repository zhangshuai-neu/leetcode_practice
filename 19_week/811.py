class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        # 类型转化处理
        domain_dict = {}
        for cp_domain in cpdomains:
            domian_list = cp_domain.split(' ')
            domain_time = int(domian_list[0])
            sub_domain_list = domian_list[1].split('.')
            
            # mail, com 转化成 mail.com, com的形式
            sdl_len = len(sub_domain_list)
            for i in range(sdl_len-1):
                for j in range(i+1,sdl_len):
                    sub_domain_list[i] = sub_domain_list[i]+"."+sub_domain_list[j]
                
            for sub_domain in sub_domain_list:
                if sub_domain not in domain_dict:
                    domain_dict.update({sub_domain:domain_time})
                else:
                    domain_dict[sub_domain] = domain_dict[sub_domain] + domain_time
        # 处理成字符串
        ret_list = []
        for domain in domain_dict:
            s = str(domain_dict[domain])+" "+domain
            ret_list.append(s)
        return ret_list
