from telethon import events
import random
from TelethonPbx.utils.basic import get_text
from TelethonPbx.plugins import *


rtext = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
]

remoji = [
    "⁭\n                    💖\n                  💖💖\n               💖💖💖\n            💖💖 💖💖\n          💖💖    💖💖\n        💖💖       💖💖\n      💖💖💖💖💖💖\n     💖💖💖💖💖💖💖\n   💖💖                 💖💖\n  💖💖                    💖💖\n💖💖                       💖💖\n",
    "⁭\n💗💗💗💗💗💗💗\n💗💗💗💗💗💗💗💗\n💗💗                     💗💗\n💗💗                     💗💗\n💗💗💗💗💗💗💗💗\n💗💗💗💗💗💗💗💗\n💗💗                     💗💗\n💗💗                     💗💗\n💗💗💗💗💗💗💗💗\n💗💗💗💗💗💗💗\n",
    "⁭\n          💛💛💛💛💛💛\n     💛💛💛💛💛💛💛💛\n   💛💛                      💛💛\n 💛💛\n💛💛\n💛💛\n 💛💛\n   💛💛                      💛💛\n     💛💛💛💛💛💛💛💛\n         💛💛💛💛💛💛\n",
    "⁭\n💙💙💙💙💙💙💙\n💙💙💙💙💙💙💙💙\n💙💙                      💙💙\n💙💙                         💙💙\n💙💙                         💙💙\n💙💙                         💙💙\n💙💙                         💙💙\n💙💙                      💙💙\n💙💙💙💙💙💙💙💙\n💙💙💙💙💙💙💙\n",
    "⁭\n💟💟💟💟💟💟💟💟\n💟💟💟💟💟💟💟💟\n💟💟\n💟💟\n💟💟💟💟💟💟\n💟💟💟💟💟💟\n💟💟\n💟💟\n💟💟💟💟💟💟💟💟\n💟💟💟💟💟💟💟💟\n",
    "⁭\n💚💚💚💚💚💚💚💚\n💚💚💚💚💚💚💚💚\n💚💚\n💚💚\n💚💚💚💚💚💚\n💚💚💚💚💚💚\n💚💚\n💚💚\n💚💚\n💚💚\n",
    "⁭\n          💜💜💜💜💜💜\n     💜💜💜💜💜💜💜💜\n   💜💜                     💜💜\n 💜💜\n💜💜                💜💜💜💜\n💜💜                💜💜💜💜\n 💜💜                        💜💜\n   💜💜                      💜💜\n     💜💜💜💜💜💜💜💜\n          💜💜💜💜💜💜\n",
    "⁭\n💖💖                        💖💖\n💖💖                        💖💖\n💖💖                        💖💖\n💖💖                        💖💖\n💖💖💖💖💖💖💖💖💖\n💖💖💖💖💖💖💖💖💖\n💖💖                        💖💖\n💖💖                        💖💖\n💖💖                        💖💖\n💖💖                        💖💖\n",
    "⁭\n💗💗💗💗💗💗\n💗💗💗💗💗💗\n          💗💗\n          💗💗\n          💗💗\n          💗💗\n          💗💗\n          💗💗\n💗💗💗💗💗💗\n💗💗💗💗💗💗\n",
    "⁭\n         💛💛💛💛💛💛\n         💛💛💛💛💛💛\n                  💛💛\n                  💛💛\n                  💛💛\n                  💛💛\n💛💛          💛💛\n  💛💛       💛💛\n   💛💛💛💛💛\n      💛💛💛💛\n",
    "⁭\n💙💙                  💙💙\n💙💙             💙💙\n💙💙        💙💙\n💙💙   💙💙\n💙💙💙💙\n💙💙 💙💙\n💙💙     💙💙\n💙💙         💙💙\n💙💙              💙💙\n💙💙                   💙💙\n",
    "⁭\n💟💟\n💟💟\n💟💟\n💟💟\n💟💟\n💟💟\n💟💟\n💟💟\n💟💟💟💟💟💟💟💟\n💟💟💟💟💟💟💟💟\n",
    "⁭\n💚💚                              💚💚\n💚💚💚                      💚💚💚\n💚💚💚💚            💚💚💚💚\n💚💚    💚💚    💚💚    💚💚\n💚💚        💚💚💚        💚💚\n💚💚             💚             💚💚\n💚💚                              💚💚\n💚💚                              💚💚\n💚💚                              💚💚\n💚💚                              💚💚\n",
    "⁭\n💜💜                           💜💜\n💜💜💜                       💜💜\n💜💜💜💜                 💜💜\n💜💜  💜💜               💜💜\n💜💜     💜💜            💜💜\n💜💜         💜💜        💜💜\n💜💜             💜💜    💜💜\n💜💜                 💜💜💜💜\n💜💜                     💜💜💜\n💜💜                          💜💜\n",
    "⁭\n           💖💖💖💖💖\n     💖💖💖💖💖💖💖\n   💖💖                   💖💖\n 💖💖                       💖💖\n💖💖                         💖💖\n💖💖                         💖💖\n 💖💖                       💖💖\n   💖💖                   💖💖\n      💖💖💖💖💖💖💖\n            💖💖💖💖💖\n",
    "⁭\n💗💗💗💗💗💗💗\n💗💗💗💗💗💗💗💗\n💗💗                     💗💗\n💗💗                     💗💗\n💗💗💗💗💗💗💗💗\n💗💗💗💗💗💗💗\n💗💗\n💗💗\n💗💗\n💗💗\n",
    "⁭\n           💛💛💛💛💛\n      💛💛💛💛💛💛💛\n   💛💛                    💛💛\n 💛💛                        💛💛\n💛💛                           💛💛\n💛💛              💛💛     💛💛\n 💛💛               💛💛 💛💛\n   💛💛                   💛💛\n      💛💛💛💛💛💛💛💛\n           💛💛💛💛💛   💛💛\n",
    "⁭\n💙💙💙💙💙💙💙\n💙💙💙💙💙💙💙💙\n💙💙                     💙💙\n💙💙                     💙💙\n💙💙💙💙💙💙💙💙\n💙💙💙💙💙💙💙\n💙💙    💙💙\n💙💙         💙💙\n💙💙              💙💙\n💙💙                  💙💙\n",
    "⁭\n       💟💟💟💟💟\n  💟💟💟💟💟💟💟\n  💟💟                 💟💟\n💟💟\n  💟💟💟💟💟💟\n      💟💟💟💟💟💟\n                            💟💟\n💟💟                 💟💟\n  💟💟💟💟💟💟💟\n       💟💟💟💟💟\n",
    "⁭\n💚💚💚💚💚💚💚💚\n💚💚💚💚💚💚💚💚\n               💚💚\n               💚💚\n               💚💚\n               💚💚\n               💚💚\n               💚💚\n               💚💚\n",
    "⁭\n💜💜                      💜💜\n💜💜                      💜💜\n💜💜                      💜💜\n💜💜                      💜💜\n💜💜                      💜💜\n💜💜                      💜💜\n💜💜                      💜💜\n  💜💜                  💜💜\n      💜💜💜💜💜💜\n            💜💜💜💜\n",
    "⁭\n💖💖                              💖💖\n  💖💖                          💖💖\n    💖💖                      💖💖\n      💖💖                  💖💖\n         💖💖              💖💖\n           💖💖         💖💖\n             💖💖     💖💖\n               💖💖 💖💖\n                  💖💖💖\n                       💖\n",
    "⁭\n💗💗                               💗💗\n💗💗                               💗💗\n💗💗                               💗💗\n💗💗                               💗💗\n💗💗              💗            💗💗\n 💗💗           💗💗          💗💗\n 💗💗        💗💗💗       💗💗\n  💗💗   💗💗  💗💗   💗💗\n   💗💗💗💗      💗💗💗💗\n    💗💗💗             💗💗💗\n",
    "⁭\n💛💛                    💛💛\n   💛💛              💛💛\n      💛💛        💛💛\n         💛💛  💛💛\n            💛💛💛\n            💛💛💛\n         💛💛 💛💛\n      💛💛       💛💛\n   💛💛             💛💛\n💛💛                   💛💛\n",
    "⁭\n💙💙                    💙💙\n   💙💙              💙💙\n      💙💙        💙💙\n         💙💙  💙💙\n            💙💙💙\n              💙💙\n              💙💙\n              💙💙\n              💙💙\n              💙💙\n",
    "⁭\n 💟💟💟💟💟💟💟\n 💟💟💟💟💟💟💟\n                       💟💟\n                   💟💟\n               💟💟\n           💟💟\n       💟💟\n   💟💟\n💟💟💟💟💟💟💟\n💟💟💟💟💟💟💟\n",
    "⁭\n       💗💗💗💗\n   💗💗💗💗💗💗\n💗💗               💗💗\n💗💗               💗💗\n💗💗               💗💗\n💗💗               💗💗\n💗💗               💗💗\n💗💗               💗💗\n   💗💗💗💗💗💗\n        💗💗💗💗\n",
    "⁭\n          💙💙\n     💙💙💙\n💙💙 💙💙\n          💙💙\n          💙💙\n          💙💙\n          💙💙\n          💙💙\n     💙💙💙💙\n     💙💙💙💙\n",
    "⁭\n    💟💟💟💟💟\n  💟💟💟💟💟💟\n💟💟          💟💟\n                💟💟\n             💟💟\n          💟💟\n       💟💟\n    💟💟\n  💟💟💟💟💟💟\n  💟💟💟💟💟💟\n",
    "⁭\n     💛💛💛💛\n  💛💛💛💛💛\n💛💛         💛💛\n                   💛💛\n            💛💛💛\n            💛💛💛\n                   💛💛\n💛💛         💛💛\n  💛💛💛💛💛\n     💛💛💛💛\n",
    "⁭\n                         💖💖\n                    💖💖💖\n              💖💖 💖💖\n          💖💖     💖💖\n     💖💖          💖💖\n💖💖               💖💖\n💖💖💖💖💖💖💖💖💖\n💖💖💖💖💖💖💖💖💖\n                         💖💖\n                         💖💖\n",
    "⁭\n💚💚💚💚💚💚\n💚💚💚💚💚💚\n💚💚\n 💚💚💚💚💚\n   💚💚💚💚💚\n                    💚💚\n                    💚💚\n💚💚          💚💚\n  💚💚💚💚💚\n     💚💚💚💚\n",
    "⁭\n        💜💜💜💜\n    💜💜💜💜💜\n💜💜\n\n💜💜\n💜💜💜💜💜💜\n💜💜💜💜💜💜💜\n💜💜               💜💜\n💜💜               💜💜\n    💜💜💜💜💜💜\n        💜💜💜💜\n",
    "⁭\n💗💗💗💗💗💗💗\n💗💗💗💗💗💗💗\n                      💗💗\n                     💗💗\n                   💗💗\n                 💗💗\n               💗💗\n             💗💗\n           💗💗\n         💗💗\n",
    "⁭\n        💙💙💙💙\n   💙💙💙💙💙💙\n💙💙               💙💙\n💙💙               💙💙\n   💙💙💙💙💙💙\n   💙💙💙💙💙💙\n💙💙               💙💙\n💙💙               💙💙\n   💙💙💙💙💙💙\n        💙💙💙💙\n",
    "⁭\n        💟💟💟💟\n   💟💟💟💟💟💟\n💟💟               💟💟\n💟💟               💟💟\n 💟💟💟💟💟💟💟\n      💟💟💟💟💟💟\n                         💟💟\n                        💟💟\n  💟💟💟💟💟💟\n       💟💟💟💟\n",
]

rtemoji = [
    "⁭\n                    {cj}\n                  {cj}{cj}\n               {cj}{cj}{cj}\n            {cj}{cj} {cj}{cj}\n          {cj}{cj}    {cj}{cj}\n        {cj}{cj}       {cj}{cj}\n      {cj}{cj}{cj}{cj}{cj}{cj}\n     {cj}{cj}{cj}{cj}{cj}{cj}{cj}\n   {cj}{cj}                 {cj}{cj}\n  {cj}{cj}                    {cj}{cj}\n{cj}{cj}                       {cj}{cj}\n",
    "⁭\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}                     {cj}{cj}\n{cj}{cj}                     {cj}{cj}\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}                     {cj}{cj}\n{cj}{cj}                     {cj}{cj}\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n",
    "⁭\n          {cj}{cj}{cj}{cj}{cj}{cj}\n     {cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n   {cj}{cj}                      {cj}{cj}\n {cj}{cj}\n{cj}{cj}\n{cj}{cj}\n {cj}{cj}\n   {cj}{cj}                      {cj}{cj}\n     {cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n         {cj}{cj}{cj}{cj}{cj}{cj}\n",
    "⁭\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}                      {cj}{cj}\n{cj}{cj}                         {cj}{cj}\n{cj}{cj}                         {cj}{cj}\n{cj}{cj}                         {cj}{cj}\n{cj}{cj}                         {cj}{cj}\n{cj}{cj}                      {cj}{cj}\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n",
    "⁭\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}\n{cj}{cj}\n{cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}\n{cj}{cj}\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n",
    "⁭\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}\n{cj}{cj}\n{cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}\n{cj}{cj}\n{cj}{cj}\n{cj}{cj}\n",
    "⁭\n          {cj}{cj}{cj}{cj}{cj}{cj}\n     {cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n   {cj}{cj}                     {cj}{cj}\n {cj}{cj}\n{cj}{cj}                {cj}{cj}{cj}{cj}\n{cj}{cj}                {cj}{cj}{cj}{cj}\n {cj}{cj}                        {cj}{cj}\n   {cj}{cj}                      {cj}{cj}\n     {cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n          {cj}{cj}{cj}{cj}{cj}{cj}\n",
    "⁭\n{cj}{cj}                        {cj}{cj}\n{cj}{cj}                        {cj}{cj}\n{cj}{cj}                        {cj}{cj}\n{cj}{cj}                        {cj}{cj}\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}                        {cj}{cj}\n{cj}{cj}                        {cj}{cj}\n{cj}{cj}                        {cj}{cj}\n{cj}{cj}                        {cj}{cj}\n",
    "⁭\n{cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}{cj}{cj}{cj}{cj}\n          {cj}{cj}\n          {cj}{cj}\n          {cj}{cj}\n          {cj}{cj}\n          {cj}{cj}\n          {cj}{cj}\n{cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}{cj}{cj}{cj}{cj}\n",
    "⁭\n         {cj}{cj}{cj}{cj}{cj}{cj}\n         {cj}{cj}{cj}{cj}{cj}{cj}\n                  {cj}{cj}\n                  {cj}{cj}\n                  {cj}{cj}\n                  {cj}{cj}\n{cj}{cj}          {cj}{cj}\n  {cj}{cj}       {cj}{cj}\n   {cj}{cj}{cj}{cj}{cj}\n      {cj}{cj}{cj}{cj}\n",
    "⁭\n{cj}{cj}                  {cj}{cj}\n{cj}{cj}             {cj}{cj}\n{cj}{cj}        {cj}{cj}\n{cj}{cj}   {cj}{cj}\n{cj}{cj}{cj}{cj}\n{cj}{cj} {cj}{cj}\n{cj}{cj}     {cj}{cj}\n{cj}{cj}         {cj}{cj}\n{cj}{cj}              {cj}{cj}\n{cj}{cj}                   {cj}{cj}\n",
    "⁭\n{cj}{cj}\n{cj}{cj}\n{cj}{cj}\n{cj}{cj}\n{cj}{cj}\n{cj}{cj}\n{cj}{cj}\n{cj}{cj}\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n",
    "⁭\n{cj}{cj}                              {cj}{cj}\n{cj}{cj}{cj}                      {cj}{cj}{cj}\n{cj}{cj}{cj}{cj}            {cj}{cj}{cj}{cj}\n{cj}{cj}    {cj}{cj}    {cj}{cj}    {cj}{cj}\n{cj}{cj}        {cj}{cj}{cj}        {cj}{cj}\n{cj}{cj}             {cj}             {cj}{cj}\n{cj}{cj}                              {cj}{cj}\n{cj}{cj}                              {cj}{cj}\n{cj}{cj}                              {cj}{cj}\n{cj}{cj}                              {cj}{cj}\n",
    "⁭\n{cj}{cj}                           {cj}{cj}\n{cj}{cj}{cj}                       {cj}{cj}\n{cj}{cj}{cj}{cj}                 {cj}{cj}\n{cj}{cj}  {cj}{cj}               {cj}{cj}\n{cj}{cj}     {cj}{cj}            {cj}{cj}\n{cj}{cj}         {cj}{cj}        {cj}{cj}\n{cj}{cj}             {cj}{cj}    {cj}{cj}\n{cj}{cj}                 {cj}{cj}{cj}{cj}\n{cj}{cj}                     {cj}{cj}{cj}\n{cj}{cj}                          {cj}{cj}\n",
    "⁭\n           {cj}{cj}{cj}{cj}{cj}\n     {cj}{cj}{cj}{cj}{cj}{cj}{cj}\n   {cj}{cj}                   {cj}{cj}\n {cj}{cj}                       {cj}{cj}\n{cj}{cj}                         {cj}{cj}\n{cj}{cj}                         {cj}{cj}\n {cj}{cj}                       {cj}{cj}\n   {cj}{cj}                   {cj}{cj}\n      {cj}{cj}{cj}{cj}{cj}{cj}{cj}\n            {cj}{cj}{cj}{cj}{cj}\n",
    "⁭\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}                     {cj}{cj}\n{cj}{cj}                     {cj}{cj}\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}\n{cj}{cj}\n{cj}{cj}\n{cj}{cj}\n",
    "⁭\n           {cj}{cj}{cj}{cj}{cj}\n      {cj}{cj}{cj}{cj}{cj}{cj}{cj}\n   {cj}{cj}                    {cj}{cj}\n {cj}{cj}                        {cj}{cj}\n{cj}{cj}                           {cj}{cj}\n{cj}{cj}              {cj}{cj}     {cj}{cj}\n {cj}{cj}               {cj}{cj} {cj}{cj}\n   {cj}{cj}                   {cj}{cj}\n      {cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n           {cj}{cj}{cj}{cj}{cj}   {cj}{cj}\n",
    "⁭\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}                     {cj}{cj}\n{cj}{cj}                     {cj}{cj}\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}    {cj}{cj}\n{cj}{cj}         {cj}{cj}\n{cj}{cj}              {cj}{cj}\n{cj}{cj}                  {cj}{cj}\n",
    "⁭\n       {cj}{cj}{cj}{cj}{cj}\n  {cj}{cj}{cj}{cj}{cj}{cj}{cj}\n  {cj}{cj}                 {cj}{cj}\n{cj}{cj}\n  {cj}{cj}{cj}{cj}{cj}{cj}\n      {cj}{cj}{cj}{cj}{cj}{cj}\n                            {cj}{cj}\n{cj}{cj}                 {cj}{cj}\n  {cj}{cj}{cj}{cj}{cj}{cj}{cj}\n       {cj}{cj}{cj}{cj}{cj}\n",
    "⁭\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n               {cj}{cj}\n               {cj}{cj}\n               {cj}{cj}\n               {cj}{cj}\n               {cj}{cj}\n               {cj}{cj}\n               {cj}{cj}\n",
    "⁭\n{cj}{cj}                      {cj}{cj}\n{cj}{cj}                      {cj}{cj}\n{cj}{cj}                      {cj}{cj}\n{cj}{cj}                      {cj}{cj}\n{cj}{cj}                      {cj}{cj}\n{cj}{cj}                      {cj}{cj}\n{cj}{cj}                      {cj}{cj}\n  {cj}{cj}                  {cj}{cj}\n      {cj}{cj}{cj}{cj}{cj}{cj}\n            {cj}{cj}{cj}{cj}\n",
    "⁭\n{cj}{cj}                              {cj}{cj}\n  {cj}{cj}                          {cj}{cj}\n    {cj}{cj}                      {cj}{cj}\n      {cj}{cj}                  {cj}{cj}\n         {cj}{cj}              {cj}{cj}\n           {cj}{cj}         {cj}{cj}\n             {cj}{cj}     {cj}{cj}\n               {cj}{cj} {cj}{cj}\n                  {cj}{cj}{cj}\n                       {cj}\n",
    "⁭\n{cj}{cj}                               {cj}{cj}\n{cj}{cj}                               {cj}{cj}\n{cj}{cj}                               {cj}{cj}\n{cj}{cj}                               {cj}{cj}\n{cj}{cj}              {cj}            {cj}{cj}\n {cj}{cj}           {cj}{cj}          {cj}{cj}\n {cj}{cj}        {cj}{cj}{cj}       {cj}{cj}\n  {cj}{cj}   {cj}{cj}  {cj}{cj}   {cj}{cj}\n   {cj}{cj}{cj}{cj}      {cj}{cj}{cj}{cj}\n    {cj}{cj}{cj}             {cj}{cj}{cj}\n",
    "⁭\n{cj}{cj}                    {cj}{cj}\n   {cj}{cj}              {cj}{cj}\n      {cj}{cj}        {cj}{cj}\n         {cj}{cj}  {cj}{cj}\n            {cj}{cj}{cj}\n            {cj}{cj}{cj}\n         {cj}{cj} {cj}{cj}\n      {cj}{cj}       {cj}{cj}\n   {cj}{cj}             {cj}{cj}\n{cj}{cj}                   {cj}{cj}\n",
    "⁭\n{cj}{cj}                    {cj}{cj}\n   {cj}{cj}              {cj}{cj}\n      {cj}{cj}        {cj}{cj}\n         {cj}{cj}  {cj}{cj}\n            {cj}{cj}{cj}\n              {cj}{cj}\n              {cj}{cj}\n              {cj}{cj}\n              {cj}{cj}\n              {cj}{cj}\n",
    "⁭\n {cj}{cj}{cj}{cj}{cj}{cj}{cj}\n {cj}{cj}{cj}{cj}{cj}{cj}{cj}\n                       {cj}{cj}\n                   {cj}{cj}\n               {cj}{cj}\n           {cj}{cj}\n       {cj}{cj}\n   {cj}{cj}\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n",
    "⁭\n       {cj}{cj}{cj}{cj}\n   {cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}               {cj}{cj}\n{cj}{cj}               {cj}{cj}\n{cj}{cj}               {cj}{cj}\n{cj}{cj}               {cj}{cj}\n{cj}{cj}               {cj}{cj}\n{cj}{cj}               {cj}{cj}\n   {cj}{cj}{cj}{cj}{cj}{cj}\n        {cj}{cj}{cj}{cj}\n",
    "⁭\n          {cj}{cj}\n     {cj}{cj}{cj}\n{cj}{cj} {cj}{cj}\n          {cj}{cj}\n          {cj}{cj}\n          {cj}{cj}\n          {cj}{cj}\n          {cj}{cj}\n     {cj}{cj}{cj}{cj}\n     {cj}{cj}{cj}{cj}\n",
    "⁭\n    {cj}{cj}{cj}{cj}{cj}\n  {cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}          {cj}{cj}\n                {cj}{cj}\n             {cj}{cj}\n          {cj}{cj}\n       {cj}{cj}\n    {cj}{cj}\n  {cj}{cj}{cj}{cj}{cj}{cj}\n  {cj}{cj}{cj}{cj}{cj}{cj}\n",
    "⁭\n     {cj}{cj}{cj}{cj}\n  {cj}{cj}{cj}{cj}{cj}\n{cj}{cj}         {cj}{cj}\n                   {cj}{cj}\n            {cj}{cj}{cj}\n            {cj}{cj}{cj}\n                   {cj}{cj}\n{cj}{cj}         {cj}{cj}\n  {cj}{cj}{cj}{cj}{cj}\n     {cj}{cj}{cj}{cj}\n",
    "⁭\n                         {cj}{cj}\n                    {cj}{cj}{cj}\n              {cj}{cj} {cj}{cj}\n          {cj}{cj}     {cj}{cj}\n     {cj}{cj}          {cj}{cj}\n{cj}{cj}               {cj}{cj}\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n                         {cj}{cj}\n                         {cj}{cj}\n",
    "⁭\n{cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}\n {cj}{cj}{cj}{cj}{cj}\n   {cj}{cj}{cj}{cj}{cj}\n                    {cj}{cj}\n                    {cj}{cj}\n{cj}{cj}          {cj}{cj}\n  {cj}{cj}{cj}{cj}{cj}\n     {cj}{cj}{cj}{cj}\n",
    "⁭\n        {cj}{cj}{cj}{cj}\n    {cj}{cj}{cj}{cj}{cj}\n{cj}{cj}\n\n{cj}{cj}\n{cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}               {cj}{cj}\n{cj}{cj}               {cj}{cj}\n    {cj}{cj}{cj}{cj}{cj}{cj}\n        {cj}{cj}{cj}{cj}\n",
    "⁭\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n                      {cj}{cj}\n                     {cj}{cj}\n                   {cj}{cj}\n                 {cj}{cj}\n               {cj}{cj}\n             {cj}{cj}\n           {cj}{cj}\n         {cj}{cj}\n",
    "⁭\n        {cj}{cj}{cj}{cj}\n   {cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}               {cj}{cj}\n{cj}{cj}               {cj}{cj}\n   {cj}{cj}{cj}{cj}{cj}{cj}\n   {cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}               {cj}{cj}\n{cj}{cj}               {cj}{cj}\n   {cj}{cj}{cj}{cj}{cj}{cj}\n        {cj}{cj}{cj}{cj}\n",
    "⁭\n        {cj}{cj}{cj}{cj}\n   {cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}               {cj}{cj}\n{cj}{cj}               {cj}{cj}\n {cj}{cj}{cj}{cj}{cj}{cj}{cj}\n      {cj}{cj}{cj}{cj}{cj}{cj}\n                         {cj}{cj}\n                        {cj}{cj}\n  {cj}{cj}{cj}{cj}{cj}{cj}\n       {cj}{cj}{cj}{cj}\n",
]


@Pbx_cmd(pattern="randomtext(?:\s|$)([\s\S]*)")
async def random_text(event):
    text = "".join(random.choices(rtext, k=10))  # Generate random 10-character string
    await event.reply(f"Random Text: {text}")

@Pbx_cmd(pattern="randomemoji(?:\s|$)([\s\S]*)")
async def random_emoji(event):
    emoji = random.choice(remoji)
    await event.reply(f"Random Emoji:\n{emoji}")


@Pbx_cmd(pattern="emoji(?:\s|$)([\s\S]*)")
async def emoji(event):
    """Message ko emoji me convert karega"""
    op = await event.reply("`Emojifying the text..`")  # Reply to user
    args = get_text(event.message)  # Extract text from message

    if not args:
        if event.reply_to and event.reply_to.text:
            args = event.reply_to.text  # Reply message se text le lo
        else:
            return await op.edit("__Mujhe koi text toh do, tabhi emoji banayunga!__")

    result = ""
    for char in args.lower():
        if char in rtext:
            result += remoji[rtext.index(char)]
        else:
            result += char  # Agar match nahi toh same character add karega

    await op.edit(result)  # Converted text ko edit karke send karega