import { Component } from '@angular/core';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.sass']
})
export class HeaderComponent {
  headerLinks = [
    'about',
    'press',
    'videos',
  ];
  iconLinks = [
    'https://www.facebook.com/TheEnglishProjectFunk/',
    'https://www.youtube.com/channel/UCnGSZ8JYM_uqTuNaJAmgeVA'
  ];
}
