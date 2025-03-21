import { Routes } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { NotfoundComponent } from './notfound/notfound.component';
import { ProductsComponent } from './products/products.component';
import { RegisterComponent } from './register/register.component';
import { ProductInfoComponent } from './product-info/product-info.component';

export const routes: Routes = [
    // path ->component 
    
    {path:'products',component:ProductsComponent},
    {path:'product/:id', component: ProductInfoComponent },
    {path:'login',component:LoginComponent},
    {path:'register',component:RegisterComponent},
    {path:'**',component:NotfoundComponent},
    
];
