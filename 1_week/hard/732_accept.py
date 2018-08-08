class MyCalendarThree:

    def __init__(self):
        book_list = []
        book_segment_count = 0

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: int
        节点存储：start,end,count以三元组的形式存放在book_list中
        """
        if book_segment_count==0:
			#book
			book_list.append(start)
			book_list.append(end)
			book_intersects=1
			book_list.append(book_intersects)
			#book数
			book_segment_count=book_segment_count+1
        else:
			new_start=start
			new_end=end
			new_index=0
			while new_index < book_segment_count:
				#左侧无交叉
				if new_end<book_list[new_index*3+0]:					
					new_book_intersects=1
					book_list.insert(new_index*3,new_book_intersects)
					book_list.insert(new_index*3,new_end)
					book_list.insert(new_index*3,new_start)
					book_segment_count=book_segment_count+1
					break
				
				#左侧交叉
				if new_start<=book_list[new_index*3+0] && new_end<book_list[new_index*3+1]:
					current_start=book_list[new_index*3+0]
					current_end=book_list[new_index*3+1]
					current_count=book_list[new_index*3+2]
					#剩余
					book_list[new_index*3+0]=new_end
					#交叉
					new_book_intersects=current_count+1
					book_list.insert(new_index*3,new_book_intersects)
					book_list.insert(new_index*3,current_start)
					book_list.insert(new_index*3,new_end)
					book_segment_count=book_segment_count+1
					#前面
					if new_start<book_list[new_index*3+0]:
						new_book_intersects=1
						book_list.insert(new_index*3,new_book_intersects)
						book_list.insert(new_index*3,current_start)
						book_list.insert(new_index*3,new_start)
						book_segment_count=book_segment_count+1
					break
					
				#中间包含
				if new_start>book_list[new_index*3+0] && new_end<=book_list[new_index*3+1]:
					current_start=book_list[new_index*3+0]
					current_end=book_list[new_index*3+1]
					current_count=book_list[new_index*3+2]
					#后面
					if new_end<book_list[new_index*3+1]:
						new_book_intersects=current_count
						book_list[new_index*3+0]=new_end
					#中间
					new_book_intersects=current_count+1
					book_list.insert(new_index*3,new_book_intersects)
					book_list.insert(new_index*3,new_end)
					book_list.insert(new_index*3,new_start)
					book_segment_count=book_segment_count+1
					#前面
					new_book_intersects=current_count
					book_list.insert(new_index*3,new_book_intersects)
					book_list.insert(new_index*3,new_start)
					book_list.insert(new_index*3,current_start)
					book_segment_count=book_segment_count+1
					break
				
				#中间相等
				if new_start==book_list[new_index*3+0] && new_end==book_list[new_index*3+1]:
					book_list[new_index*3+2]=book_list[new_index*3+2]+1
					break
				
				#右侧交叉
				if new_start<book_list[new_index*3+1] && new_start<book_list[new_index*3+1]:
					current_start=book_list[new_index*3+0]
					current_end=book_list[new_index*3+1]
					current_count=book_list[new_index*3+2]
					#前面
					book_list[new_index*3+1]=new_start
					new_index=new_index+1
					#交叉
					new_book_intersects=current_count+1
					book_list.insert(new_index*3,new_book_intersects)
					book_list.insert(new_index*3,current_end)
					book_list.insert(new_index*3,new_start)
					book_segment_count=book_segment_count+1
					new_index=new_index+1
					#后面,交给下一轮处理
					new_start=current_end
					
				#右侧无交叉
				if new_start>=book_list[new_index*3+1]:
					#交给下一轮处理
					new_index=new_index+1
					if new_index>book_segment_count:
						
					

		#最大intersects
		max_intersects=0
		i=0
		while i<book_segment_count:
			if max_intersects<boo_list[i*3+2]:
				max_intersects=boo_list[i*3+2]
			
		return max_intersects	
		
		
        
        


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)	


MyCalendarThree();
MyCalendarThree.book(10, 20); // returns 1
MyCalendarThree.book(50, 60); // returns 1
MyCalendarThree.book(10, 40); // returns 2
MyCalendarThree.book(5, 15); // returns 3
MyCalendarThree.book(5, 10); // returns 3
MyCalendarThree.book(25, 55); // returns 3
