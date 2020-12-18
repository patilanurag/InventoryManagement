from django.contrib import admin
from .models import Record,GreyQualityMaster,GreyCheckerMaster,GreyCutRange,ProcessingPartyNameMaster,GreyArrivalLocationMaster,ColorAndChemicalsSupplier,Color,ColorRecord,ChemicalsDailyConsumption,ChemicalsAllOrders,ChemicalsGodownLooseMergeStock,ChemicalsGodownsMaster,ChemicalsLooseGodownMaster,ChemicalsUnitsMaster,ChemicalsClosingStock
from .models import Employee,MonthlyPayment,CompanyAccounts,ChemicalsClosingStockperGodown,GreyTransportMaster,CityMaster,EmployeeCategoryMaster
from import_export.admin import ImportExportModelAdmin
# Register your models here.

@admin.register(Employee,EmployeeCategoryMaster,MonthlyPayment,CityMaster,ChemicalsClosingStockperGodown,CompanyAccounts,GreyTransportMaster,Record,GreyQualityMaster,GreyCheckerMaster,GreyCutRange,ProcessingPartyNameMaster,GreyArrivalLocationMaster,ColorAndChemicalsSupplier,Color,ColorRecord,ChemicalsDailyConsumption,ChemicalsAllOrders,ChemicalsGodownLooseMergeStock,ChemicalsGodownsMaster,ChemicalsLooseGodownMaster,ChemicalsUnitsMaster,ChemicalsClosingStock)

class ItemAdmin(ImportExportModelAdmin):
    pass