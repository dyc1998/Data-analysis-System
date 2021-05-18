import pandas as pd
import os
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

def dataPreprocessing():####---1
    while True:
        fileName=input('请输入要打开的文件(house.sale.price.csv)：')
        try:
            #读取csv文件，将数据导入到df中
            df = pd.read_csv(fileName,encoding='cp936')
            #drop的意思是删除，na的意思是空值（缺失值），合起来就是删除缺失值的意思,然后将删除后的值赋值给df_new
            df_new=df.dropna()
            print('缺失值去除成功！')
            print('下面展示前三行的内容:')
            print(df_new.head(3))
            print('下面展示后两行的内容:')
            print(df_new.tail(2))
        except FileNotFoundError:#--这个except仅仅处理没有找到文件的错误。
            ans = input('没有找到您要查询的文件，请检查您的输入，您是否继续输入(y/n):')
            if ans == 'y':
                continue
            else:
                break
        except:
            print('任务一执行失败,请重新开始！')
            continue
        else:
            print('任务1执行成功！')
            break

def dataSelection():#-------2
    while True:
        #输入要打开的文件
        fileName=input('请输入要打开的文件名(house.sale.price.csv)：')
        try:
            df=pd.read_csv(fileName,encoding='cp936')#读取数据
            feature_columns=['Id','MSZoning','LotArea','YrSold','SalePrice']#定义要保存的列，存到一个列表中
            df_new=df.loc[:,feature_columns]#-取这几列的数据
            try:
                outname = input('请输入要导出的文件名(house_total_price.txt)：')
                #按要求将数据保存
                df_new.to_csv(outname,encoding='cp936',
                              index=False,sep=' ')
                print('文件导出成功')
            except:#如果出现错误，那么报错显示文件导入错误
                print('文件导出失败！')
                continue
        except FileNotFoundError:  # --这个except仅仅处理没有找到文件的错误。
                ans = input('没有找到您要查询的文件，请检查您的输入，您是否继续输入(y/n):')
                if ans == 'y':
                    continue
                else:
                    break
        except:
            print('任务2执行失败！')
        else:
            print('任务2执行成功')
            break

def dataCalculate():#------3
    while True:
        #要打开的文件名
        filename=input('请输入要打开的文件名(house_total_price.txt)：')
        try:
            df=pd.read_csv(filename,encoding='cp936',delimiter=' ')#读取数据到df中
            df['unitPrice']=df['SalePrice']/df['LotArea']#计算两列的商，并且添加到unitPrice这个新列中
            try:
                outname = input('请输入要导出的文件名(house_unit_price.xlsx)：')
                df.to_excel(outname,encoding='cp936',index=False)
                print('excel导出完毕!')
            except:#如果报错，那就显示文件导入失败
                print('excel导出失败!')
        except FileNotFoundError:# --这个except仅仅处理没有找到文件的错误。
            ans = input('没有找到您要查询的文件，请检查您的输入，您是否继续输入(y/n):')
            if ans == 'y':
                continue
            else:
                break
        except:
            print('任务3执行失败！')
            
        else:
            print('任务3执行成功!')
            break

def  dataDescribeVisualization():#-----4
    while True:
        filename=input('请输入要读取的文件名(house_unit_price.xlsx)：')
        try:
            df=pd.read_excel(filename)#-读取数据
            df_group = df.groupby('MSZoning').mean()#----以MSZoning分组并且求均值（mean)
            df_sort = df_group.sort_values(by='unitPrice', ascending=False)#进行数据的排序
            #name是来坐x轴的轴刻度，将其转化成列表（list)
            name=list(df_sort.index)
            name.append('NA')#-----这个题有歧义，我单独加的NA列
            #同样，将y轴的数据也进行列表处理
            nums=list(df_sort['unitPrice'])
            nums.append(0)#---NA的值为0，因为都已经当成缺失值去掉了
            #--所画柱状图的一些设置
            plt.figure(figsize=(10, 10))#画布的大小为10*10
            plt.bar(x=name, height=nums, width=0.5)
            plt.xticks(fontsize=15)#-------x轴轴刻度的字体大小
            plt.title('房屋类型与每平米均价关系图', size=20)#---整个图的大标题
            plt.xlabel('MSZoning', size=15)#-----x轴的名称
            plt.ylabel('unitPrice', size=15)#-y轴的名称
            plt.legend(['每平米价格'])#--所谓的图例
            #为了可以再柱状图上显示出数据，因为matplotlib所画的柱状图不能将数值显示在柱子上面，所以要单独写函数
            for a, b in zip(name, nums):
                plt.text(a, b + 0.05, '%.4f' % b, ha='center', va='bottom', fontsize=15)
            figname=input('请输入要保存图片的名称(house_unit_price.png)：')
            plt.savefig(figname,dpi=400)
            plt.show()

        except FileNotFoundError:#如果要读取的文件没找到，就输出这个报错信息
            ans = input('没有找到您要查询的文件，请检查您的输入，您是否继续输入(y/n):')
            if ans == 'y':
                continue
            else:
                break
        except:
            print('任务4执行失败！')
        else:
            print('任务4执行成功！')
            break

def dataVisualization():#--------5
    while True:
        filename=input('请输入读取的文件名(house_unit_price.xlsx)：')
        try:
            df = pd.read_excel(filename)
            df_group = df.groupby('YrSold').mean()
            name = df_group.index
            nums = df_group['unitPrice']
            plt.figure(figsize=(10, 15))
            plt.bar(x=name, height=nums, width=0.5)
            plt.title('每平米价格与年份统计图', size=20)
            plt.xlabel('YrSold', size=15)
            plt.xticks(size=14)
            plt.ylabel('unitPrice', size=15)
            plt.ylim([0,30])
            plt.legend(['年度均价'])
            for a, b in zip(name, nums):
                plt.text(a, b + 0.05, '%.4f' % b, ha='center', va='bottom', fontsize=15)
            outname = input('请输入要导出的文件名(house_year_price.png)：')
            plt.savefig(outname, dpi=400)
            plt.show()
            print('导出文件成功！')
        except FileNotFoundError:
            ans = input('没有找到您要查询的文件，请检查您的输入，您是否继续输入(y/n):')
            if ans == 'y':
                continue
            else:
                break
        else:
            print('任务5执行成功！')
            break


def menu():
    print('【任务选择】\n'
          '+--------2006-2010年不同类型房屋售价数据分析及可视化系统----------+\n'
          '|0、退出。                                                        |\n'
          '|1、数据读取及预处理。                                            |\n'
          '|2、数据选择及导出。                                              |\n'
          '|3、数据计算并添加。                                              |\n'
          '|4、数据统计和观察。                                              |\n'
          '|5、数据可视化。                                                  |\n'
          '+-----------------------------------------------------------------+')
def task():
    while True:
        menu()
        num=input('请输入任务选择：')
        if num=='1':
            dataPreprocessing()
        elif num=='2':
            if os.path.exists('house.sale.price.csv'):
                dataSelection()
            else:
                print('未能执行当前的选项，请先执行之前的选项')

        # elif num=='3':
        #     if os.path.exists('house.sale.price.csv'):
        #         dataGroup()
        #     else:
        #         print('未能执行当前的选项，请先执行之前的选项')

        elif num=='3':
            if os.path.exists('house.sale.price.csv'):
                dataCalculate()
            else:
                print('未能执行当前的选项，请先执行之前的选项')
        elif num=='4':
            if os.path.exists('house.sale.price.csv'):
                dataDescribeVisualization()
            else:
                print('未能执行当前的选项，请先执行之前的选项')
        elif num=='5':
            if os.path.exists('house.sale.price.csv'):
                dataVisualization()
            else:
                print('未能执行当前的选项，请先执行之前的选项')
        elif num=='0':
            answer=input('你是否要退出系统？y/n')
            if answer=='y':
                print('程序结束！')
                break
            elif answer=='n':
                continue
        else:
            print('您的输入不符合要求！')
        input('按回车键显示菜单')

if __name__ == '__main__':
    task()
