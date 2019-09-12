 import java.util.*;
//数组排序之后相邻数的最大差值
public class MaxMinusArr{
	//方法一、获得相邻数的最大差值
    public static int getMaxMinusArr(int[]arr)
    {
           int max=Integer.MIN_VALUE;
           if(arr==null||arr.length<2)
           {
            	 return -1;
           }
           for(int i=0;i<arr.length-1;i++)
           {  
           	   int k=arr[i+1]-arr[i];
           	   max=Math.max(max,k);
           }
          return max;
          
    }
    //方法二(基于桶排序的思想)
    public static int getMaxMinusArr02(int[]arr)
    {
          if(arr==null||arr.length<2)
          {
          	 return -1;
          }
          int len=arr.length; //数组的长度
          int min=Integer.MAX_VALUE;
          int max=Integer.MIN_VALUE;
          for(int i=0;i<len;i++)
          {
          	  min=Math.min(min,arr[i]); //获得数组中的最小值
          	  max=Math.max(max,arr[i]); //获得数组中的最大值
          }
          if(min==max)
          {
          	 return 0;
          }
          boolean[]hasNum=new boolean[len+1];
          int[]maxs=new int[len+1];
          int[]mins=new int[len+1];
          int bid=0;
           for(int i=0;i<len;i++)
           {
           	  bid=bucket(arr[i],len,min,max); //算出桶号
           	  mins[bid] = hasNum[bid] ? Math.min(mins[bid], arr[i]) : arr[i];
           	  maxs[bid] = hasNum[bid] ? Math.min(maxs[bid], arr[i]) : arr[i];
              hasNum[bid]=true;
           }
           int res=0;
           int lasMax=maxs[0];
           int  i=1;
           for(;i<=len;i++)
           {
           	   if(hasNum[i])
           	   {
           	   	 res=Math.max(res,mins[i]-lasMax);
           	     lasMax=maxs[i];
           	   }
           }
          return res;
    }
    //使用long类型防止相乘时溢出,获得当前数需要放置的桶位置
    public static int bucket(long num,long len,long min,long max)
    {
            return (int)((num-min)*len/(max-min));
    }
    public static int[]generateArr(int size)
    {
    	 int[]arr=new int[size];
    	 for(int i=0;i<size;i++)
    	 {
    	 	  arr[i]=(int)(Math.random()*100);
    	 }
    	 Arrays.sort(arr);
    	 return arr;
    }
    //打印生成的矩阵
    public static void printArr(int[]arr)
    {
    	for(int i=0;i<arr.length;i++)
    	{
    		System.out.print(arr[i]+" ");
    	}
        System.out.println();
    }
	public static void main(String[]args)
	{      int size=20;
           int[]arr=generateArr(size);
           printArr(arr);
           System.out.println(getMaxMinusArr(arr));
           System.out.println(getMaxMinusArr02(arr));
	}
}