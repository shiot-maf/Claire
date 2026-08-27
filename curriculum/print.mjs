/* 학습지 → 인쇄용 PDF.
 *
 *   node print.mjs worksheets/report-technology.html print/이름_교사용.pdf
 *   node print.mjs worksheets/report-technology.html print/이름_학생용.pdf student
 *
 * 「선생님께」를 끈 상태로 뽑으려면 마지막에 student 를 붙인다. 쪽 나눔은
 * 두 상태가 같으므로 같은 쪽에 같은 활동이 온다.
 *
 * 화면용 CSS가 아니라 @media print 를 태워야 그림자·툴바가 빠지므로
 * emulateMedia 를 먼저 부른다. preferCSSPageSize 는 @page{size:A4;margin:0}
 * 을 따르게 해 여백이 두 번 들어가는 것을 막는다.
 *
 * 필요한 것: playwright-core 와 크로미움. 없으면
 *   npm i playwright-core && npx playwright install chromium
 */
import { chromium } from 'playwright-core';
import path from 'node:path';

const [src, out, mode] = process.argv.slice(2);
if (!src || !out) {
  console.error('사용법: node print.mjs <입력.html> <출력.pdf> [student]');
  process.exit(1);
}

const browser = await chromium.launch({
  executablePath: process.env.CHROME_PATH || undefined,
});
const page = await browser.newPage();
await page.goto('file://' + path.resolve(src));
try {
  await page.waitForFunction(() => document.fonts.status === 'loaded', { timeout: 10000 });
} catch { /* 웹폰트가 늦으면 대체 서체로 뽑힌다 */ }

if (mode === 'student') {
  await page.evaluate(() => {
    const cb = document.getElementById('tt');
    if (cb) { cb.checked = false; cb.dispatchEvent(new Event('change')); }
    document.body.classList.add('hide-notes');
  });
}

await page.emulateMedia({ media: 'print' });
await page.waitForTimeout(300);
await page.pdf({ path: out, format: 'A4', printBackground: true, preferCSSPageSize: true });
await browser.close();
console.log(out, mode === 'student' ? '· 학생용' : '· 교사용');
