import pandas as pd


class Read_File:
    def __init__(self, filename):
        self.filename = filename

    def readexcel(self):
        excel_file = '../excel_file/' + self.filename
        data = pd.read_excel(excel_file)
        return data

    def readtxt(self):
        txt_file = '../txt_file/' + self.filename
        data = pd.read_table(txt_file)
        return data

    def readcsv(self):
        pass

    def readword(self):
        pass

    def readpdf(self):
        pass

    def main(self):
        filename_split = self.filename.split('.')
        name_type = filename_split[-1]
        if name_type == 'xlsx':
            print('文件类型为：', name_type)
            data = self.readexcel()

            # data['compon'] = data['日期'].map(str) + ',' + data['质量等级'].map(str) + ',' + data['No2'].map(str)
            #
            # # data['compon'].to_csv('../txt_file/data.txt',sep='\n',index=False)
            #
            # data.to_excel('../excel_file/data1.xlsx')
            #
            # # data.head(3) # 打印前3行
            # # data[1:3] # 打印[1,3)行数据
            # # data['日期'] # 打印某一列数据
            # # data[['日期','质量等级']] # 打印多列数据
            # # data.columns.tolist() # 查看所有列名 : 列表形式
            # # data.loc[4] # 只显示第四行，以series结构显示（一维数据结构）
        elif name_type == 'txt':
            print('文件类型为：', name_type)
            data = self.readtxt()
        elif name_type == 'csv':
            print('文件类型为：', name_type)
            data = self.readcsv()
        else:
            print('该文件属于其他类型')
            print('文件类型为：', name_type)
            data = False
        return data

# beg_to_read = Read_File('data.xlsx')
# data = beg_to_read.main()
# print(data)
