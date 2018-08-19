class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        simple_path = "/"
        path_list = []

        #生成以 / 分割的list
        #按照 "dir/" 格式进行处理
        #如果最后不符合，在21行进行处理
        path_len = len(path)
        i = 1
        temp_str = ""
        while i<path_len:
            if path[i] != '/':
                temp_str = temp_str + path[i]
            if path[i] == '/':    #生成字符串，并去除"///"类似情况
                if temp_str != "":
                    path_list.append(temp_str)
                temp_str = ""
            i=i+1
        if temp_str != "":
            path_list.append(temp_str)

        #处理 "." 和 ".."
        print(path_list)
        i=0
        path_list_len = len(path_list)
        while i < path_list_len:
            if path_list[i]==".":
                path_list.pop(i)
                path_list_len = path_list_len-1
            else:
                if path_list[i]=="..":
                    if i!=0:            #删除前一个，/的".."为/
                        i=i-1
                        path_list.pop(i)
                        path_list_len = path_list_len-1
                    path_list.pop(i)    #删除".."
                    path_list_len = path_list_len-1
                else:
                    i=i+1

        #生成简化path
        for i in range(len(path_list)):
            if i < len(path_list)-1:
                simple_path = simple_path + path_list[i] + "/"
            else:
                simple_path = simple_path + path_list[i]

        return simple_path
