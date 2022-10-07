import { Injectable, Res } from '@nestjs/common';
import { HttpService } from '@nestjs/axios';

import * as fs from 'fs';

@Injectable()
export class AppService {
  constructor(private readonly httpService: HttpService) {}
  getHello(): string {
    return 'Hello World!';
  }
  async getImg(@Res() res): Promise<any> {
    const writer = fs.createWriteStream('./images/image.png');

    const response = await this.httpService.axiosRef({
        url: 'https://www.nautiljon.com/images/perso/00/20/gon_freecss_12702.jpg',
        method: 'GET',
        responseType: 'stream',
    });

    response.data.pipe(writer);

    return new Promise((resolve, reject) => {
        writer.on('finish', resolve);
        writer.on('error', reject);
    });
}
}
