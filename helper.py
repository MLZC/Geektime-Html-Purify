removeElementsList = ['#gkui-message-list', '#gkui-modal-controller', '#app > div._2sRsF5RP_0', 'body > svg', '#app > div._1ysv2txS_0._2bUO5eUH_0 > div._3-b6SqNP_0', '#app > div._1ysv2txS_0._2bUO5eUH_0 > div._1Q_izgym_0 > div.rBDXhMZ0_0', '#app > div._1ysv2txS_0._2bUO5eUH_0 > div._1Q_izgym_0 > div._35V_pofE_0', '#app > div._1ysv2txS_0._2bUO5eUH_0 > div._1Q_izgym_0 > div.k7LpsVQS_0', '#app > div > div > div > div > div.simplebar-wrapper > div.simplebar-mask > div > div > div > div > div._2SKlnZlt_0 > div._1QFlQFbV_0.EdaaidhQ_0',
                      '#app > div._1ysv2txS_0._2bUO5eUH_0 > div._1Q_izgym_0 > div.ibY_sXau_0 > div > div.simplebar-wrapper > div.simplebar-mask > div > div > div > div > div._2Vlfl3UO_0', '#app > div._1ysv2txS_0._2bUO5eUH_0 > div._1Q_izgym_0 > div.ibY_sXau_0 > div > div.simplebar-wrapper > div.simplebar-mask > div > div > div > div > div._2SKlnZlt_0 > div._23_U6jTI_0', '#app > div._1ysv2txS_0._2bUO5eUH_0 > div._1Q_izgym_0 > div.ibY_sXau_0 > div > div.simplebar-wrapper > div.simplebar-mask > div > div > div > div > div._2SKlnZlt_0 > div._2sg1Tei__0', '#app > div > div > div > div > div.simplebar-track.simplebar-horizontal', '#app > div > div > div > div > div.simplebar-track.simplebar-vertical', '#app > div > div > div > div > div.simplebar-wrapper > div.simplebar-mask > div > div > div > div > div._3-W_zrq4_0 > div', '#app > div > div > div > div > div.simplebar-wrapper > div.simplebar-mask > div > div > div > div > div._2SKlnZlt_0 > div._1kh1ihh6_0._2i1ytqT9_0 > div._2w-W27j5_0', '#app > div > div > div > div > div.simplebar-wrapper > div.simplebar-mask > div > div > div > div > div._2SKlnZlt_0 > div._1kh1ihh6_0._2i1ytqT9_0 > div.zbKHG1ec_0']
style = """
._1ysv2txS_0 {
position: initial !important;
overflow: visible !important;
}
._1Q_izgym_0{
position: initial !important;
overflow: visible !important;
}
.ibY_sXau_0 {
position: initial !important;
overflow: visible !important;
}
@media print{
.simplebar-track.simplebar-vertical{visibility: hidden !important;}
}
"""

script = """
var elems = document.getElementsByClassName('simplebar-placeholder');
myElement = elems[elems.length - 1];
console.log(myElement)
myElement.style.height = document.getElementsByClassName('simplebar-content')[0].offsetHeight + 'px';
"""
