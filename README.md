# AI Scaling in iRacing
The addition of AI to iRacing has made it possible to race whatever you want wherever you want, no longer being restricted to the tracks iRacing chooses for you in a certain season. Before starting a race, you will be given the option to choose a difficulty for the AI. This difficulty is, however, not related to an expected lap time and the difficulty that's right for you may differ from track to track and car to car. In order to investigate the effect of the difficulty slider on the AI lap times, a series of qualifying sessions was run with a Mercedes-AMG GT3 EVO and a Porsche 963 at 20 different difficulty levels. Scaling was found to follow
$$D=-\tau_D\ln\left[\frac{t_w}{t_tA_1}\left(f_0+A_1\exp\left(-\frac{D_t}{\tau_D}\right)\right)-\frac{f_0}{A_1}\right]$$
with an associated error given by
$$S_D^2 =  \left(\left[-\ln\xi-\frac{t_w D}{\xi t_t \tau_D}\exp\left(-\frac{D}{\tau_D}\right)\right]S_{\tau_D}\right)^2  + \left(-\frac{\tau_D}{\xi}\left(\frac{t_w}{t_tA_1}-\frac{1}{A_1}\right)S_{f_0}\right)^2 + \left(-\frac{\tau_D}{\xi}\left[-\frac{t_wf_0}{t_tA_1^2} + \frac{f_o}{A_1^2}\right]S_{A_1}\right)^2.$$
## Calculate Spread
This repository contains all information used in the calculation of the AI scaling for iRacing. If you would like to calculate the AI spread for another track please follow the following instructions
1. Copy the contents of the `AItestingRoster.rar` archive to your `Documents` folder
2. Open iRacing and create a new AI session (or season)
3. Pick the track(s) you are interested in
4. Choose the `AI Testing` opponents filter
5. Set the spread of AI to 0 % - 100 %
6. Run a qualifying session followed by a race. When the race has started you can exit the session
7. When returning to the iRacing UI, click `Export Results` in the bottom left
8. Copy the `parse.py` script to the same folder you saved the results to
9. Open a new terminal in the parse.py folder
10. Run `python parse.py results.json` and replace `results` by the name you saved the results under
This will create a `results.txt` file containing the difficulty and qualifying times in your session. 00 - 100 indicates the difficulty level in GTP. 500 - 600 indicates the difficulty in GTD, subtract 500 from the car number to find the difficulty percentage for the car and driver.
## Storage
All information used in the creation of this repository is contained in the `AITimingResults.xlsx` spreadsheet. You can add your own information to further improve the dataset.
## Derivation and Calculator
All background information, derivation, and a calculator can be found here: https://josapol.web.app/JSPGaming/iRAIScaling.html.
