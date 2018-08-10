class MyCalendarThree:
    def __init__(self):
        self.book_list = []
        self.book_segment_count = 0

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: int
        节点存储：start,end,count以三元组的形式存放在book_list中
        """
       
        if self.book_segment_count==0:
            #book
            self.book_list.append(start)
            self.book_list.append(end)
            book_intersects=1
            self.book_list.append(book_intersects)
            #book数
            self.book_segment_count=self.book_segment_count+1
        else:
            new_start=start
            new_end=end
            new_index=0
            while new_index <= self.book_segment_count:
				#添加到最末尾
                if new_index == self.book_segment_count:
                    print("debug_zs2")
                    new_book_intersects=1
                    self.book_list.insert(new_index*3,new_book_intersects)
                    self.book_list.insert(new_index*3,new_end)
                    self.book_list.insert(new_index*3,new_start)
                    self.book_segment_count=self.book_segment_count+1
                    break
				
                current_start=self.book_list[new_index*3+0]
                current_end=self.book_list[new_index*3+1]
                current_count=self.book_list[new_index*3+2]
                
                #new_start在current_book 左侧
                if new_start<current_start:
                    #无交叉
                    if new_end<=current_start:                
                        new_book_intersects=1
                        self.book_list.insert(new_index*3,new_book_intersects)
                        self.book_list.insert(new_index*3,new_end)
                        self.book_list.insert(new_index*3,new_start)
                        self.book_segment_count=self.book_segment_count+1
                        break
                    #交叉
                    if new_end<=current_end:
                        #剩余
                        self.book_list[new_index*3+0]=new_end
                        #交叉
                        new_book_intersects=current_count+1
                        self.book_list.insert(new_index*3,new_book_intersects)
                        self.book_list.insert(new_index*3,new_end)
                        self.book_list.insert(new_index*3,current_start)
                        self.book_segment_count=self.book_segment_count+1
                        #前面
                        new_book_intersects=1
                        self.book_list.insert(new_index*3,new_book_intersects)
                        self.book_list.insert(new_index*3,current_start)
                        self.book_list.insert(new_index*3,new_start)
                        self.book_segment_count=self.book_segment_count+1
                        break
                    #超过 new_end>current_end:
                    #前面
                    new_book_intersects=1
                    self.book_list.insert(new_index*3,new_book_intersects)
                    self.book_list.insert(new_index*3,current_start)
                    self.book_list.insert(new_index*3,new_start)
                    self.book_segment_count=self.book_segment_count+1
                    new_index=new_index+1
                    #交叉
                    self.book_list[new_index*3+2]=current_count+1
                    new_index=new_index+1
                    #剩余
                    new_start=current_end
                    
                    continue
                
                #new_start在current_book中间
                if new_start<current_end:
                    if new_end<=current_end:
                        if new_start==current_start and new_end==current_end:
                            self.book_list[new_index*3+2]=self.book_list[new_index*3+2]+1
                            break
                        if new_start==current_start and new_end!=current_end:
                            #后面
                            new_book_intersects=current_count
                            self.book_list[new_index*3+0]=new_end
                            #交叉
                            new_book_intersects=current_count+1
                            self.book_list.insert(new_index*3,new_book_intersects)
                            self.book_list.insert(new_index*3,new_end)
                            self.book_list.insert(new_index*3,new_start)
                            self.book_segment_count=self.book_segment_count+1
                            break
                        if new_start!=current_start and new_end==current_end:
                            #交叉
                            new_book_intersects=current_count+1
                            self.book_list[new_index*3+0]=new_start
                            self.book_list[new_index*3+2]=new_book_intersects
                            #前面
                            new_book_intersects=current_count
                            self.book_list.insert(new_index*3,new_book_intersects)
                            self.book_list.insert(new_index*3,new_start)
                            self.book_list.insert(new_index*3,current_start)
                            self.book_segment_count=self.book_segment_count+1
                            break
                        #后面
                        new_book_intersects=current_count
                        self.book_list[new_index*3+0]=new_end
                        #中间
                        new_book_intersects=current_count+1
                        self.book_list.insert(new_index*3,new_book_intersects)
                        self.book_list.insert(new_index*3,new_end)
                        self.book_list.insert(new_index*3,new_start)
                        self.book_segment_count=self.book_segment_count+1
                        #前面
                        new_book_intersects=current_count
                        self.book_list.insert(new_index*3,new_book_intersects)
                        self.book_list.insert(new_index*3,new_start)
                        self.book_list.insert(new_index*3,current_start)
                        self.book_segment_count=self.book_segment_count+1
                        break
                        
                    if new_end>current_end:
                        if new_start>current_start:
                            #前面
                            self.book_list[new_index*3+1]=new_start
                            new_index=new_index+1
                            #中间
                            new_book_intersects=current_count+1
                            self.book_list.insert(new_index*3,new_book_intersects)
                            self.book_list.insert(new_index*3,current_end)
                            self.book_list.insert(new_index*3,new_start)
                            self.book_segment_count=self.book_segment_count+1
                            new_index=new_index+1
                        else:
                            self.book_list[new_index*3+2]=current_count+1
                            new_index=new_index+1
                        #后面,下一轮处理
                        new_start=current_end
    
                        continue
                    
                #new_start在current_book右侧
                if new_start>=current_end:
                    #交给下一轮处理
                    new_index=new_index+1

        #最大intersects
        max_intersects=0
        i=0
        while i<self.book_segment_count:
            if max_intersects<self.book_list[i*3+2]:
                max_intersects=self.book_list[i*3+2]
            i=i+1

        return max_intersects  
