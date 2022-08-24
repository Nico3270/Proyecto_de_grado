from mimetypes import init
from scipy.interpolate import lagrange

tabla_9x = [10,20,30,40,50,60,70,80,90,100]
plano = {0.5:{40:[1.00, 1.00, 1.04, 1.10, 1.12, 1.13, 1.14, 1.13, 1.14, 1.14], 50:[1.00,1.00,1.04,1.10,1.12,1.13,1.14,1.13,1.14,1.14],
60:[1.01,1.16,1.18,1.20,1.21,1.21,1.20,1.19,1.19,1.18],70:[1.43,1.42,1.36,1.34,1.32,1.30,1.28,1.27,1.26,1.24], 
80:[1.86,1.65,1.52,1.46,1.42,1.38,1.36,1.33,1.31,1.30],90:[2.16,1.80,1.62,1.54,1.49,1.44,1.40,1.37,1.35,1.33]},
1:{40:[1.00,1.00,1.04,1.10,1.12,1.13,1.14,1.13,1.14,1.14],50:[1.00,1.00,1.04,1.10,1.12,1.13,1.14,1.13,1.14,1.14],
60:[1.09,1.21,1.22,1.23,1.24,1.23,1.22,1.21,1.20,1.20],70:[1.67,1.54,1.45,1.41,1.38,1.35,1.32,1.30,1.29,1.27],
80:[2.26,1.85,1.66,1.57,1.51,1.46,1.42,1.39,1.36,1.34],90:[2.57,2.02,1.77,1.65,1.58,1.52,1.47,1.43,1.41,1.38]},
1.5:{40:{1.00,1.00,1.04,1.10,1.12,1.13,1.14,1.13,1.14,1.14},50:[1.00,1.00,1.05,1.10,1.13,1.14,1.14,1.14,1.14,1.14],
60:[1.13,1.23,1.23,1.24,1.24,1.23,1.22,1.21,1.21,1.20],70:[1.79,1.61,1.49,1.44,1.41,1.37,1.34,1.32,1.30,1.29],
80:[2.50,1.98,1.74,1.63,1.56,1.50,1.46,1.42,1.40,1.37],90:[2.93,2.20,1.89,1.75,1.66,1.59,1.53,1.48,1.45,1.42]},
2:{40:[1.00,1.00,1.04,1.10,1.12,1.13,1.14,1.13,1.14,1.14],50:[1.00,1.02,1.06,1.11,1.14,1.14,1.15,1.14,1.15,1.14],
60:[1.13,1.23,1.23,1.24,1.24,1.23,1.22,1.21,1.21,1.20],70:[1.84,1.63,1.51,1.45,1.42,1.38,1.35,1.32,1.31,1.29],
80:[2.50,1.98,1.74,1.63,1.56,1.50,1.46,1.42,1.40,1.37],90:[2.99,2.23,1.91,1.77,1.67,1.60,1.54,1.49,1.46,1.43]},
2.5:{40:[1.00,1.00,1.04,1.10,1.12,1.13,1.14,1.13,1.14,1.14],50:[1.00,1.02,1.06,1.11,1.14,1.14,1.15,1.14,1.15,1.14],
60:[1.13,1.23,1.23,1.24,1.24,1.23,1.22,1.21,1.21,1.20],70:[1.84,1.63,1.51,1.45,1.42,1.38,1.35,1.32,1.31,1.29],
80:[2.60,2.03,1.78,1.66,1.58,1.52,1.48,1.43,1.41,1.38],90:[3.04,2.26,1.93,1.78,1.68,1.61,1.55,1.50,1.47,1.44]},
3:{40:[1.00,1.00,1.04,1.10,1.12,1.13,1.14,1.13,1.14,1.14],50:[1.00,1.02,1.06,1.11,1.14,1.14,1.15,1.14,1.15,1.14],
60:[1.13,1.23,1.23,1.24,1.24,1.23,1.22,1.21,1.21,1.20],70:[1.84,1.63,1.51,1.45,1.42,1.38,1.35,1.32,1.31,1.29],
80:[2.65,2.06,1.79,1.67,1.60,1.53,1.48,1.44,1.42,1.39],90:[3.09,2.28,1.95,1.79,1.69,1.62,1.53,1.51,1.47,1.44]},
3.5:{40:[1.00,1.00,1.04,1.10,1.12,1.13,1.14,1.13,1.14,1.14],50:[1.00,1.02,1.06,1.11,1.14,1.14,1.15,1.14,1.15,1.14],
60:[1.13,1.23,1.23,1.24,1.24,1.23,1.22,1.21,1.21,1.20],70:[1.84,1.63,1.51,1.45,1.42,1.38,1.35,1.32,1.31,1.29],
80:[2.65,2.06,1.79,1.67,1.60,1.53,1.48,1.44,1.42,1.39],90:[3.09,2.28,1.95,1.79,1.69,1.62,1.56,1.51,1.47,1.44]}}
ondulado = {0.5:{20:[1.00, 1.00,1.04,1.10,1.12,1.13,1.14,1.13,1.14,1.14],30:[1.00,1.00,1.04,1.10,1.12,1.13,1.14,1.13,1.14,1.14],
40:[1.00,1.00,1.04,1.10,1.12,1.13,1.14,1.13,1.14,1.14],50:[1.01,1.12,1.16,1.19,1.20,1.19,1.19,1.18,1.18,1.18],
60:[1.51,1.46,1.39,1.36,1.34,1.32,1.30,1.28,1.27,1.25],70:[2.03,1.74,1.58,1.51,1.46,1.42,1.38,1.35,1.34,1.32],
80:[2.57,2.01,1.77,1.65,1.58,1.52,1.47,1.43,1.41,1.31]},1:{20:[1.00,1.00,1.04,1.10,1.12,1.13,1.14,1.13,1.14,1.14],
30:[1.00,1.00,1.04,1.10,1.12,1.13,1.14,1.13,1.14,1.14],40:[1.00,1.00,1.05,1.10,1.13,1.14,1.14,1.14,1.14,1.14],
50:[1.24,1.29,1.27,1.27,1.27,1.26,1.24,1.23,1.22,1.20],60:[2.14,1.79,1.61,1.53,1.48,1.44,1.40,1.37,1.35,1.33],
70:[2.88,2.17,1.87,1.74,1.65,1.58,1.52,1.48,1.45,1.42],80:[3.68,2.59,2.16,1.95,1.83,1.73,1.65,1.59,1.55,1.51],
80:[3.68,2.59,2.16,1.95,1.83,1.73,1.65,1.59,1.55,1.51]},1.5:{20:[1.00,1.00,1.04,1.10,1.12,1.13,1.14,1.13,1.14,1.14],
30:[1.00,1.00,1.04,1.10,1.12,1.13,1.14,1.13,1.14,1.14],40:[1.00,1.03,1.08,1.12,1.14,1.15,1.15,1.15,1.15,1.15],
50:[1.44,1.43,1.37,1.35,1.33,1.31,1.29,1.27,1.26,1.25],60:[2.45,1.95,1.72,1.62,1.55,1.50,1.45,1.41,1.39,1.37],
70:[3.44,2.47,2.07,1.89,1.77,1.68,1.61,1.56,1.52,1.48],80:[4.31,2.92,2.38,2.13,1.97,1.85,1.76,1.68,1.63,1.59]},
2:{20:[1.00,1.00,1.04,1.10,1.12,1.13,1.14,1.13,1.14,1.14],30:[1.00,1.00,1.04,1.10,1.12,1.13,1.14,1.13,1.14,1.14],
40:[1.00,1.03,1.08,1.12,1.14,1.15,1.15,1.15,1.15,1.15],50:[1.48,1.45,1.38,1.36,1.34,1.31,1.29,1.27,1.26,1.25],
60:[2.54,2.00,1.76,1.65,1.57,1.51,1.47,1.43,1.40,1.38],70:[3.50,2.50,2.10,1.97,1.79,1.69,1.62,1.57,1.53,1.49],
80:[4.44,2.98,2.43,2.16,1.99,1.87,1.78,1.70,1.65,1.60]},2.5:{20:[1.00,1.00,1.04,1.10,1.12,1.13,1.14,1.13,1.14,.14],
30:[1.19,1.20,1.20,1.22,1.22,1.22,1.21,1.20,1.20,1.19],40:[2.53,1.99,1.75,1.64,1.57,1.51,1.46,1.43,1.40,1.38],
50:[4.04,2.78,2.29,2.05,1.91,1.80,1.71,1.64,1.60,1.56],60:[5.25,3.41,2.72,2.38,2.18,2.02,1.91,1.82,1.76,1.70],
70:[6.31,3.96,3.09,2.67,2.41,2.22,2.09,1.97,1.90,1.83],80:[7.71,4.41,3.40,2.91,2.60,2.39,2.23,2.10,2.01,1.93]},
3:{20:[1.00,1.00,1.04,1.10,1.12,1.13,1.14,1.13,1.14,1.14],30:[1.23,1.22,1.22,1.23,1.23,1.22,1.22,1.21,1.20,1.19],
40:[2.53,1.99,1.75,1.64,1.57,1.51,1.46,1.43,1.40,1.38],50:[4.04,2.78,2.29,2.05,1.91,1.80,1.71,1.64,1.60,1.56],
60:[5.25,3.41,2.72,2.38,2.18,2.02,1.91,1.82,1.76,1.70],70:[6.31,3.96,3.09,2.67,2.41,2.22,2.09,1.97,1.90,1.83],
80:[7.17,4.41,3.40,2.91,2.60,2.39,2.23,2.10,2.01,1.93]},3.5:{20:[1.00,1.00,1.04,1.10,1.12,1.13,1.14,1.13,1.14,1.14],
30:[1.23,1.22,1.22,1.23,1.23,1.22,1.22,1.21,1.20,1.19],40:[2.62,2.04,1.79,1.67,1.59,1.53,1.48,1.44,1.41,1.39],
50:[4.09,2.80,2.30,2.07,1.92,1.80,1.72,1.65,1.60,1.56],60:[5.33,3.45,2.74,2.40,2.19,2.04,1.92,1.83,1.77,1.71],
70:[6.40,4.01,3.12,2.70,2.43,2.24,2.10,1.99,1.91,1.81],80:[7.25,4.45,3.43,2.93,2.62,2.40,2.24,2.11,2.02,1.94]},
4:{20:[1.00,1.00,1.04,1.10,1.12,1.13,1.14,1.13,1.14,1.14],30:[1.23,1.24,1.23,1.24,1.24,1.23,1.22,1.21,1.21,1.20],
40:[2.67,2.07,1.80,1.68,1.60,1.54,1.49,1.45,1.42,1.39],50:[4.16,2.4,2.33,2.09,1.93,1.82,1.73,1.66,1.61,1.57],
60:[5.40,3.49,2.77,2.42,2.21,2.05,1.94,1.84,1.78,1.72],70:[6.49,4.05,3.15,2.72,2.45,2.26,2.12,2.00,1.92,1.85],
80:[7.35,4.50,3.46,2.95,2.64,2.42,2.26,2.13,2.03,1.95]},4.5:{20:[1.00,1.00,1.04,1.10,1.12,1.13,1.14,1.13,1.14,1.14],
30:[1.23,1.24,1.23,1.24,1.24,1.23,1.22,1.21,1.21,1.20],40:[2.67,2.07,1.80,1.68,1.60,1.54,1.49,1.45,1.42,1.39],
50:[4.16,2.84,2.33,2.09,1.93,1.82,1.73,1.66,1.61,1.57],60:[5.40,3.49,2.77,2.42,2.21,2.05,1.94,1.84,1.78,1.72],
70:[6.49,4.05,3.15,2.72,2.45,2.26,2.12,2.00,1.92,1.85],80:[7.45,4.55,3.50,2.98,2.67,2.44,2.27,2.14,2.05,1.96]}}
montanoso = {0.5:{20:[1.00, 1.00, 1.04, 1.10, 1.12, 1.13, 1.14, 1.13,1.14,1.14],30:[1.00,1.00,1.04,1.10,1.12,1.13,1.14,1.13,1.14,1.14],
40:[1.24,1.27,1.26,1.26,1.26,1.25,1.24,1.22,1.22,1.21],50:[2.09,1.76,1.60,1.52,1.47,1.43,1.39,1.36,1.34,1.32],
60:[2.82,2.14,1.86,1.72,1.63,1.57,1.51,1.47,1.44,1.41],70:[3.60,2.55,2.13,1.93,1.81,1.71,1.64,1.58,1.54,1.50],
80:[4.31,2.92,2.38,2.13,1.97,1.85,1.76,1.68,1.63,1.59]},1:{20:[1.00,1.00,1.04,1.10,1.12,1.13,1.14,1.13,1.14,1.14],
30:[1.01,1.07,1.10,1.14,1.16,1.16,1.16,1.16,1.16,1.16],40:[2.07,1.75,1.59,1.52,1.47,1.42,1.39,1.36,1.34,1.32],
50:[3.46,2.48,2.08,1.89,1.79,1.69,1.62,1.56,1.52,1.49],60:[4.65,3.10,2.50,2.22,2.04,1.91,1.81,1.73,1.68,1.63],
70:[5.69,3.64,2.87,2.50,2.27,2.11,1.98,1.88,1.81,1.75],80:[6.64,4.13,3.21,2.76,2.49,2.29,2.14,2.02,1.94,1.87]},
1.5:{20:[1.00,1.00,1.04,1.10,1.12,1.13,1.14,1.13,1.14,1.14],30:[1.12,1.13,1.15,1.18,1.19,1.19,1.19,1.18,1.18,1.17],
40:[2.33,1.89,1.68,1.59,1.53,1.47,1.43,1.40,1.37,1.35],50:[3.74,2.62,2.18,1.97,1.84,1.74,1.66,1.60,1.56,1.52],
60:[4.91,3.23,2.60,2.29,2.10,1.96,1.86,1.77,1.71,1.66],70:[6.07,3.83,3.01,2.61,2.36,2.18,2.05,1.94,1.86,1.80],
80:[6.90,4.26,3.30,2.83,2.54,2.34,2.18,2.06,1.97,1.90]},2:{20:[1.00,1.00,1.04,1.10,1.12,1.13,1.14,1.13,1.14,1.14],
30:[1.16,1.16,1.18,1.20,1.21,1.20,1.20,1.19,1.19,1.18],40:[2.43,1.94,1.72,1.61,1.55,1.49,1.45,1.41,1.39,1.36],
50:[3.86,2.68,2.22,2.00,1.87,1.76,1.68,1.62,1.57,1.53],60:[5.12,3.34,2.67,2.35,2.15,2.00,1.89,1.80,1.74,1.68],
70:[6.16,3.88,3.04,2.63,2.38,2.20,2.06,1.95,1.88,1.81],80:[7.17,4.41,3.40,2.91,2.60,2.39,2.23,2.10,2.01,1.93]},
2.5:{20:[1.00,1.00,1.04,1.10,1.12,1.13,1.14,1.13,1.14,1.14],30:[1.19,1.20,1.20,1.22,1.22,1.22,1.21,1.20,1.20,1.19],
40:[2.53,1.99,1.75,1.64,1.57,1.51,1.46,1.43,1.40,1.38],50:[4.04,2.78,2.29,2.05,1.91,1.80,1.71,1.64,1.60,1.56],
60:[5.25,3.41,2.72,2.38,2.18,2.02,1.91,1.82,1.76,1.70],70:[6.31,3.96,3.09,2.67,2.41,2.22,2.09,1.97,1.90,1.83],
80:[7.17,4.41,3.40,2.91,2.60,2.39,2.23,2.10,2.01,1.93]},3:{20:[1.00,1.00,1.04,1.10,1.12,1.13,1.14,1.13,1.14,1.14],
30:[1.23,1.22,1.22,1.23,1.23,1.22,1.22,1.21,1.20,1.19],40:[2.53,1.99,1.75,1.64,1.57,1.51,1.46,1.43,1.40,1.38],
50:[4.04,2.78,2.29,2.05,1.91,1.80,1.71,1.64,1.60,1.56],60:[5.33,3.45,2.74,2.40,2.19,2.04,1.92,1.83,1.77,1.71],
70:[6.31,3.96,3.09,2.67,2.41,2.22,2.09,1.97,1.90,1.83],80:[7.17,4.41,3.40,2.91,2.60,2.39,2.23,2.10,2.01,1.93]},
3.5:{20:[1.00,1.00,1.04,1.10,1.12,1.13,1.14,1.13,1.14,1.14],30:[1.23,1.22,1.22,1.23,1.23,1.22,1.22,1.21,1.20,1.19],
40:[2.62,2.04,1.79,1.67,1.59,1.53,1.48,1.44,1.41,1.39],50:[4.09,2.80,2.30,2.07,1.92,1.80,1.72,1.62,1.60,1.56],
60:[5.33,3.45,2.74,2.40,2.19,2.04,1.92,1.83,1.77,1.71],70:[6.40,4.01,3.12,2.70,2.43,2.24,2.10,1.99,1.91,1.84],
80:[7.25,4.45,3.43,2.93,2.62,2.40,2.24,2.11,2.02,1.94]},4:{20:[1.00,1.00,1.04,1.10,1.12,1.13,1.14,1.13,1.14,1.14],
30:[1.23,1.24,1.23,1.24,1.24,1.23,1.22,1.21,1.21,1.20],40:[2.67,2.07,1.80,1.68,1.60,1.54,1.49,1.45,1.42,1.39],
50:[4.16,2.84,2.33,2.09,1.93,1.82,1.73,1.66,1.61,1.57],60:[5.40,3.49,2.77,2.42,2.21,2.05,1.94,1.84,1.78,1.72],
70:[6.49,4.05,3.15,2.72,2.45,2.26,2.12,2.00,1.92,1.85],80:[7.35,4.50,3.46,2.95,2.64,2.42,2.26,2.13,2.03,1.95]},
4.5:{20:[1.00,1.00,1.04,1.10,1.12,1.13,1.14,1.13,1.14,1.14],30:[1.23,1.24,1.23,1.24,1.24,1.23,1.22,1.21,1.21,1.20],
40:[2.67,2.07,1.80,1.68,1.60,1.54,1.49,1.45,1.42,1.39],50:[4.16,2.84,2.33,2.09,1.93,1.82,1.73,1.66,1.61,1.57],
60:[5.40,3.49,2.77,2.42,2.21,2.05,1.94,1.84,1.78,1.72],70:[6.49,4.05,3.15,2.72,2.45,2.26,2.12,2.00,1.92,1.85],
80:[7.45,4.55,3.50,2.98,2.67,2.44,2.27,2.14,2.05,1.96]}}
escarpado = {0.5:{10:[1.00,1.00,1.04,1.10,1.12,1.13,1.14,1.13,1.14,1.14],20:[1.03,1.07,1.10,1.14,1.16,1.16,1.16,1.16,1.16,1.15],
30:[2.10,1.77,1.60,1.52,1.47,1.43,1.39,1.36,1.34,1.32],40:[3.81,2.66,2.20,1.99,1.85,1.75,1.67,1.61,1.57,1.53],
50:[5.23,3.40,2.71,2.38,2.17,2.02,1.91,1.82,1.75,1.70],60:[6.36,3.99,3.11,2.69,2.42,2.23,2.09,1.98,1.90,1.82],
70:[6.86,4.25,3.29,2.82,2.54,2.33,2.18,2.05,1.97,1.89]},1:{10:[1.00,1.00,1.04,1.10,1.12,1.13,1.14,1.13,1.14,1.14],
20:[1.43,1.32,1.28,1.28,1.27,1.26,1.25,1.23,1.23,1.22],30:[3.52,2.51,2.10,1.91,1.79,1.70,1.63,1.57,1.53,1.49],
40:[5.36,3.46,2.75,2.41,2.20,2.04,1.93,1.84,1.77,1.71],50:[6.89,4.26,3.30,2.83,2.51,2.33,2.18,2.06,1.97,1.90],
60:[8.01,4.84,3.69,3.13,2.79,2.54,2.36,2.22,2.12,2.03],70:[8.50,5.10,3.87,3.27,2.90,2.64,2.45,2.29,2.18,2.09]},
1.5:{10:[1.00,1.00,1.04,1.10,1.12,1.13,1.14,1.13,1.14,1.14],20:[1.72,1.50,1.41,1.38,1.35,1.33,1.30,1.28,1.27,1.26],
30:[3.98,2.75,2.26,2.04,1.89,1.78,1.70,1.64,1.59,1.54],40:[5.81,3.70,2.91,2.53,2.30,2.13,2.00,1.90,1.83,1.77],
50:[7.29,4.47,3.44,2.94,2.63,2.41,2.25,2.12,2.02,1.94],60:[8.47,5.08,3.86,3.26,2.89,2.63,2.44,2.29,2.18,2.08],
70:[9.00,5.36,4.04,3.40,3.01,2.73,2.53,2.37,2.25,2.15]},2:{10:[1.00,1.00,1.04,1.10,1.12,1.13,1.14,1.13,1.14,1.14],
20:[1.83,1.58,1.46,1.42,1.39,1.36,1.33,1.31,1.29,1.28],30:[4.27,2.90,2.37,2.11,1.96,1.84,1.75,1.68,1.63,1.58],
40:[6.10,3.85,3.02,2.61,2.36,2.18,2.05,1.94,1.87,1.80],50:[7.65,4.65,3.56,3.04,2.71,2.48,2.31,2.17,2.07,1.99],
60:[8.80,5.25,3.97,3.35,2.97,2.70,2.50,2.34,2.22,2.12],70:[9.27,5.50,4.14,3.48,3.07,2.78,2.57,2.40,2.28,2.18]},
2.5:{10:[1.00,1.00,1.04,1.10,1.12,1.13,1.14,1.13,1.14,1.14],20:[1.93,1.63,1.50,1.44,1.41,1.37,1.35,1.32,1.31,1.29],
30:[4.39,2.96,2.41,2.15,1.99,1.86,1.77,1.70,1.64,1.60],40:[6.28,3.94,3.08,2.66,2.41,2.22,2.08,1.97,1.89,1.82],
50:[7.72,4.69,3.59,3.06,2.73,2.49,2.32,2.18,2.08,2.00],60:[8.87,5.29,4.00,3.37,2.98,2.71,2.51,2.35,2.23,2.13],
70:[9.35,5.54,4.17,3.50,3.09,2.80,2.59,2.42,2.29,2.19]},3:{10:[1.00,1.00,1.04,1.10,1.12,1.13,1.14,1.13,1.14,1.14],
20:[2.07,1.70,1.55,1.48,1.44,1.40,1.37,1.34,1.32,1.31],30:[4.50,3.02,2.45,2.18,2.01,1.88,1.79,1.71,1.66,1.61],
40:[6.34,3.97,3.10,2.68,2.42,2.23,2.09,1.98,1.90,1.83],50:[7.87,4.77,3.65,3.10,2.76,2.52,2.34,2.20,2.10,2.01],
60:[8.96,5.34,4.03,3.39,3.00,2.73,2.52,2.36,2.24,2.14],70:[9.44,5.58,4.20,3.52,3.11,2.81,2.60,2.43,2.31,2.20]},
3.5:{10:[1.00,1.00,1.04,1.10,1.12,1.13,1.14,1.13,1.14,1.14],20:[2.07,1.70,1.55,1.48,1.44,1.40,1.37,1.34,1.32,1.31],
30:[1.55,3.04,2.47,2.19,2.02,1.89,1.80,1.72,1.67,1.62],40:[6.54,4.08,3.17,2.73,2.46,2.27,2.12,2.01,1.93,1.85],
50:[7.94,4.81,3.67,3.12,2.78,2.53,2.35,2.21,2.11,2.02],60:[9.06,5.39,4.07,3.42,3.03,2.74,2.54,2.37,2.26,2.16],
60:[9.06,5.39,4.07,3.42,3.03,2.74,2.54,2.37,2.26,2.16],70:[9.54,5.64,4.23,3.55,3.13,2.83,2.62,2.44,2.32,2.21]},
4:{10:[1.00,1.00,1.04,1.10,1.12,1.13,1.14,1.13,1.14,1.14],20:[2.13,1.74,1.57,1.50,1.45,1.41,1.38,1.35,1.33,1.31],
30:[4.63,3.09,2.50,2.21,2.04,1.91,1.81,1.73,1.68,1.63],40:[6.59,4.11,3.19,2.75,2.48,2.28,2.13,2.02,1.93,1.86],
50:[8.02,4.85,3.70,3.14,2.79,2.55,2.37,2.22,2.12,2.03],60:[9.22,5.47,4.12,3.46,3.06,2.77,2.56,2.40,2.28,2.17],
70:[9.63,5.68,4.27,3.59,3.15,2.85,2.63,2.46,2.33,2.22]},4.5:{10:[1.00,1.00,1.04,1.10,1.12,1.13,1.14,1.13,1.14,1.14],
20:[2.17,1.76,1.58,1.51,1.46,1.42,1.39,1.36,1.34,1.32],30:[4.69,3.12,2.52,2.23,2.05,1.92,1.82,1.74,1.68,1.63],
40:[6.59,4.11,3.19,2.75,2.48,2.28,2.13,2.02,1.93,1.86],50:[8.02,4.85,3.70,3.14,2.79,2.55,2.37,2.22,2.12,2.03],
60:[9.22,5.47,4.12,3.46,3.06,2.77,2.56,2.40,2.28,2.17]}}
 

def interpolacion(x,y,z):
    p = lagrange(x,y)
    resultado = (z)
    return round(p(z),3)

def intervalos(num):
    inf = 0
    sup = 0
    list = [10,20,30,40,50,60,70,80,90]
    for x in list:
        if num - x >=0 and num - x <= 10:
            inf = x
            sup= inf + int((num-x)+(10-(num-x)))
    return(inf,sup)


#print(interpolacion(tabla_9x, punto_1, 35))

def inter_compuesta_mon_esc(v2,tab_9x, terreno,p_pesados, l_sector):
    inf = intervalos(v2)
    sup = intervalos(v2)
    int_0y5_0 =  interpolacion(tab_9x,terreno.get(0.5).get(inf),p_pesados)
    int_0y5_1 =  interpolacion(tab_9x,terreno.get(0.5).get(sup),p_pesados)
    resultado_1 = interpolacion([inf,sup],[int_0y5_0,int_0y5_1],v2)
    int_1_0 =  interpolacion(tab_9x,terreno.get(1).get(inf),p_pesados)
    int_1_1 =  interpolacion(tab_9x,terreno.get(1).get(sup),p_pesados)
    resultado_2 = interpolacion([inf,sup],[int_1_0,int_1_1],v2)
    int_1_5_0 =  interpolacion(tab_9x,terreno.get(1.5).get(inf),p_pesados)
    int_1_5_1 =  interpolacion(tab_9x,terreno.get(1.5).get(sup),p_pesados)
    resultado_3 = interpolacion([inf,sup],[int_1_5_0,int_1_5_1],v2)
    int_2_0 =  interpolacion(tab_9x,terreno.get(2).get(inf),p_pesados)
    int_2_1 =  interpolacion(tab_9x,terreno.get(2).get(sup),p_pesados)
    resultado_4 = interpolacion([inf,sup],[int_2_0,int_2_1],v2)
    int_2_5_0 =  interpolacion(tab_9x,terreno.get(2.5).get(inf),p_pesados)
    int_2_5_1 =  interpolacion(tab_9x,terreno.get(2.5).get(sup),p_pesados)
    resultado_5 = interpolacion([inf,sup],[int_2_5_0,int_2_5_1],v2)
    int_3_0 =  interpolacion(tab_9x,terreno.get(3).get(inf),p_pesados)
    int_3_1 =  interpolacion(tab_9x,terreno.get(3).get(sup),p_pesados)
    resultado_6 = interpolacion([inf,sup],[int_3_0,int_3_1],v2)
    int_3_5_0 =  interpolacion(tab_9x,terreno.get(3.5).get(inf),p_pesados)
    int_3_5_1 =  interpolacion(tab_9x,terreno.get(3.5).get(sup),p_pesados)
    resultado_7 = interpolacion([inf,sup],[int_3_5_0,int_3_5_1],v2)
    int_4_0 =  interpolacion(tab_9x,terreno.get(4).get(inf),p_pesados)
    int_4_1 =  interpolacion(tab_9x,terreno.get(4).get(sup),p_pesados)
    resultado_8 = interpolacion([inf,sup],[int_4_0,int_4_1],v2)
    int_4_5_0 =  interpolacion(tab_9x,terreno.get(4.5).get(inf),p_pesados)
    int_4_5_1 =  interpolacion(tab_9x,terreno.get(4.5).get(sup),p_pesados)
    resultado_9 = interpolacion([inf,sup],[int_4_5_0,int_4_5_1],v2)
    datos_x = [0,5,1,1.5,2,2.5,3,3.5,4,4.5]
    datos = [resultado_1,resultado_2, resultado_3, resultado_4, resultado_5,
    resultado_6, resultado_7, resultado_8, resultado_9]
    return interpolacion(datos_x, datos,l_sector)

def inter_compuesta_plan_ond(v2,tab_9x, terreno,p_pesados, l_sector):
    inf = intervalos(v2)[0]
    sup = intervalos(v2)[1]
    int_0y5_0 =  interpolacion(tab_9x,terreno.get(0.5).get(inf),p_pesados)
    int_0y5_1 =  interpolacion(tab_9x,terreno.get(0.5).get(sup),p_pesados)
    resultado_1 = interpolacion([inf,sup],[int_0y5_0,int_0y5_1],v2)
    int_1_0 =  interpolacion(tab_9x,terreno.get(1).get(inf),p_pesados)
    int_1_1 =  interpolacion(tab_9x,terreno.get(1).get(sup),p_pesados)
    resultado_2 = interpolacion([inf,sup],[int_1_0,int_1_1],v2)
    int_1_5_0 =  interpolacion(tab_9x,terreno.get(1.5).get(inf),p_pesados)
    int_1_5_1 =  interpolacion(tab_9x,terreno.get(1.5).get(sup),p_pesados)
    resultado_3 = interpolacion([inf,sup],[int_1_5_0,int_1_5_1],v2)
    int_2_0 =  interpolacion(tab_9x,terreno.get(2).get(inf),p_pesados)
    int_2_1 =  interpolacion(tab_9x,terreno.get(2).get(sup),p_pesados)
    resultado_4 = interpolacion([inf,sup],[int_2_0,int_2_1],v2)
    int_2_5_0 =  interpolacion(tab_9x,terreno.get(2.5).get(inf),p_pesados) 
    int_2_5_1 =  interpolacion(tab_9x,terreno.get(2.5).get(sup),p_pesados)
    resultado_5 = interpolacion([inf,sup],[int_2_5_0,int_2_5_1],v2)
    int_3_0 =  interpolacion(tab_9x,terreno.get(3).get(inf),p_pesados)
    int_3_1 =  interpolacion(tab_9x,terreno.get(3).get(sup),p_pesados)
    resultado_6 = interpolacion([inf,sup],[int_3_0,int_3_1],v2)
    int_3_5_0 =  interpolacion(tab_9x,terreno.get(3.5).get(inf),p_pesados)
    int_3_5_1 =  interpolacion(tab_9x,terreno.get(3.5).get(sup),p_pesados)
    resultado_7 = interpolacion([inf,sup],[int_3_5_0,int_3_5_1],v2)
    datos_x =[0.5,1,1.5,2,2.5,3,3.5]
    datos = [resultado_1,resultado_2, resultado_3, resultado_4, resultado_5,
    resultado_6, resultado_7]
    return interpolacion(datos_x, datos,l_sector)

print(inter_compuesta_plan_ond(83.17,tabla_9x,plano,45,0.8))

