from abc import ABC, abstractmethod
import xlsxwriter


class excel(ABC):
    @abstractmethod
    def write_in_excel(self, info):
        pass

    
class Excel(excel):
    def write_in_excel(self, info):
    
        workbook = xlsxwriter.Workbook('info.xlsx')
        worksheet = workbook.add_worksheet()
        row = 0
        # traverse each row in info and insert data into xlsx file
        for r in info:
            col = 0
            for item in r:
                # insert into the worksheet
                worksheet.write(row, col, item)
                col+=1

            row += 1
        workbook.close()

    