from django.urls import path
from capp import views
urlpatterns = [
   path('',views.INDEX),
   path('register/',views.REGISTER),
   path('owneraccount/',views.OWNERACCOUNT),
   path('useraccount/',views.USERACCOUNT),
   path('user/',views.USER),
   path('login/',views.LOGIN),
   path('logout/',views.logout),
   # path('userlogin/',views.USERLOGIN),
   # path('userlogout/',views.userlogout),
   path('single/',views.SINGLE),
   path('feedback/',views.FEEDBACK),
   path('feedbacked/',views.FEEDBACKED),
   path('ownerview/',views.OWNERTAB),
   path('editowner/',views.OWNEREDIT),
   path('updateowner/',views.OWNERUPDATE),
   path('deleteowner/',views.OWNERDELETE),
   path('userview/',views.USERTAB),
   path('edituser/',views.USEREDIT),
   path('updateuser/',views.USERUPDATE),
   path('deleteuser/',views.USERDELETE),
   path('ownereditpassword/',views.OWNEREDITPASSWORD),
   path('ownerchangepassword/',views.OWNERCHANGEPASSWORD),
   path('forgotpassword/',views.FORGOTPASSWORD),
   path('usereditpassword/',views.USEREDITPASSWORD),
   path('userchangepassword/',views.USERCHANGEPASSWORD),
   path('products/',views.PRODUCTS),
   path('addturf/',views.ADDTURF),
   path('turftab/',views.TURFTAB),
   path('bookingtab/',views.BOOKING),
   path('editturf/',views.EDITTURF),
   path('updateturf/',views.UPDATETURF),
   path('deleteturf/',views.DELETETURF),
   path('profile/',views.PROFILE),
   path('addcart/',views.ADDCART),
   path('cart/',views.CART),
   path('remove/',views.REMOVE),
   path('removeall/',views.REMOVEALL),
   path('checkout/',views.CHECKOUT),
   path('1/',views.INDEX1),
   path('admprofile/',views.ADMPROFILE),
   path('adownertab/',views.ADOWNERTAB),
   path('signin/',views.SIGNIN),
   path('signout/',views.signout),
   path('approved/',views.APPROVED),
   path('rejected/',views.REJECTED),
   path('adcarttab/',views.ADCARTTAB),
   path('adturftab/',views.ADTURFTAB),
   path('adusertab/',views.ADUSERTAB),
   path('tapproved/',views.ADAPPROVED),
   path('trejected/',views.ADREJECTED),
   path('admprofile/',views.ADMPROFILE),
   path('2/',views.INDEX2),
   path('bookingorder/',views.BOOKINGORDER),
   path('bookedorders/',views.BOOKEDORDERS),
   path('available/',views.AVAILABLE),
   path('notavailable/',views.NOTAVAILABLE),
   path('payment/',views.PAYMENT),
   # path('contact/',views.CONTACT),
   # path('adcontacttab/',views.ADCONTACTTAB),
   



]