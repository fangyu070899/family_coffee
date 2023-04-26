def get_new_event():
  return {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://i.imgur.com/93AGehx.jpg",
        "size": "xxl",
        "aspectRatio": "1414:2000"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "露西藝伎/衣索比亞/班奇馬吉/露西處理站/頂級G1藝伎",
            "weight": "bold",
            "size": "xl"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": " NT$310 / 半磅 230g"
              },
              {
                "type": "text",
                "text": " NT$570 / 一磅 460g"
              }
            ],
            "margin": "md"
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "horizontal",
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "height": "sm",
            "action": {
              "type": "uri",
              "label": "立即購買",
              "uri": "https://supersell.fami.life/users/325772/merchandise/1763580"
            },
            "style": "primary",
            "color": "#b02e0c"
          }
        ],
        "flex": 0
      },
      "styles": {
        "body": {
          "separator": True
        }
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://i.imgur.com/vRFDBjO.jpg",
        "size": "xxl",
        "aspectRatio": "1414:2000"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "生豆/花貝果娜/紅圈計畫/西達摩/水洗首選G1/74158",
            "weight": "bold",
            "size": "xl"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": " NT$300 / 半磅 230g"
              },
              {
                "type": "text",
                "text": " NT$550 / 一磅 460g"
              },
              {
                "type": "text",
                "text": " NT$470 / 生豆 1000g"
              }
            ],
            "margin": "md"
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "horizontal",
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "height": "sm",
            "action": {
              "type": "uri",
              "label": "立即購買",
              "uri": "https://supersell.fami.life/users/325772/merchandise/1763574"
            },
            "style": "primary",
            "color": "#b02e0c"
          }
        ],
        "flex": 0
      },
      "styles": {
        "body": {
          "separator": True
        }
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://i.imgur.com/dmJGWWb.jpg",
        "size": "xxl",
        "aspectRatio": "1414:2000"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "夏茉卡/頂級G1/紅圈計畫/耶加雪菲/2023新批次/74110/水洗",
            "weight": "bold",
            "size": "xl"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": " NT$300 / 半磅 230g"
              },
              {
                "type": "text",
                "text": " NT$550 / 一磅 460g"
              }
            ],
            "margin": "md"
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "horizontal",
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "height": "sm",
            "action": {
              "type": "uri",
              "label": "立即購買",
              "uri": "https://supersell.fami.life/users/325772/merchandise/1763556"
            },
            "style": "primary",
            "color": "#b02e0c"
          }
        ],
        "flex": 0
      },
      "styles": {
        "body": {
          "separator": True
        }
      }
    }
  ]
}

def get_about_coffee():
  return {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://i.imgur.com/tbUvFuL.png",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "backgroundColor": "#FFFFFF"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "淺談咖啡",
            "weight": "bold",
            "size": "xl",
            "margin": "md"
          },
          {
            "type": "text",
            "text": "告訴你如何找到自己喜歡的咖啡",
            "margin": "md",
            "align": "start"
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "我喝的是什麼咖啡",
              "text": "我喝的是什麼咖啡?"
            },
            "height": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "影響咖啡風味的關鍵",
              "text": "影響咖啡風味的關鍵"
            },
            "height": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "如何萃取一杯好咖啡",
              "text": "如何萃取一杯好咖啡?"
            },
            "height": "sm"
          }
        ],
        "flex": 0
      },
      "styles": {
        "footer": {
          "separator": True
        }
      }
    }

def get_coffee_kind():
  return {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://i.imgur.com/tbUvFuL.png",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "backgroundColor": "#FFFFFF"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "您喝的是什麼咖啡",
            "weight": "bold",
            "size": "xl",
            "margin": "md"
          },
          {
            "type": "text",
            "text": "在這裡我們談論的是黑咖啡~",
            "margin": "md",
            "align": "start"
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "單品咖啡",
              "text": "單品咖啡"
            },
            "height": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "綜合咖啡",
              "text": "綜合咖啡"
            },
            "height": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "精品咖啡",
              "text": "精品咖啡"
            },
            "height": "sm"
          }
        ],
        "flex": 0
      },
      "styles": {
        "footer": {
          "separator": True
        }
      }
    }

def get_coffee_extract():
  return {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://i.imgur.com/4pS9f3A.png",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "backgroundColor": "#FFFFFF"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "如何萃取一杯好咖啡",
            "weight": "bold",
            "size": "xl",
            "margin": "md"
          },
          {
            "type": "text",
            "text": "咖啡與萃取之間的關係",
            "margin": "md",
            "align": "start"
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "沖煮器材",
              "text": "沖煮器材"
            },
            "height": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "粉水比",
              "text": "粉水比"
            },
            "height": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "研磨刻度與對應沖煮時間",
              "text": "研磨刻度與對應沖煮時間"
            },
            "height": "sm"
          }
        ],
        "flex": 0
      },
      "styles": {
        "footer": {
          "separator": True
        }
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://i.imgur.com/cTUCYBi.png",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "backgroundColor": "#FFFFFF"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "如何萃取一杯好咖啡",
            "weight": "bold",
            "size": "xl",
            "margin": "md"
          },
          {
            "type": "text",
            "text": "咖啡與萃取之間的關係",
            "margin": "md",
            "align": "start"
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "水質",
              "text": "水質"
            },
            "height": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "過濾器材",
              "text": "過濾器材"
            },
            "height": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "正確的溫度、時間、擾流(3T)",
              "text": "正確的溫度、時間、擾流(3T)"
            },
            "height": "sm"
          }
        ],
        "flex": 0
      },
      "styles": {
        "footer": {
          "separator": True
        }
      }
    }
  ]
}
  
def get_coffee_flavor():
  return {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://i.imgur.com/4pS9f3A.png",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "backgroundColor": "#FFFFFF"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "咖啡樹品種",
            "weight": "bold",
            "size": "xl",
            "margin": "md"
          },
          {
            "type": "text",
            "text": "目前具商業價值被大量栽種只有阿拉比卡種、羅布斯塔種及賴比瑞亞種，不同品種的咖啡豆有不同的味道，但即使是相同品種的咖啡樹，由於不同土壤、不同氣候以及海拔高度等影響，生長出的咖啡豆也各具有獨特的風味。",
            "margin": "md",
            "align": "start"
          }
        ],
        "action": {
          "type": "message",
          "label": "action",
          "text": "咖啡樹品種"
        }
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "阿拉比卡種",
              "text": "阿拉比卡種"
            },
            "height": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "羅布斯塔種",
              "text": "羅布斯塔種"
            },
            "height": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "賴比瑞亞種",
              "text": "賴比瑞亞種"
            },
            "height": "sm"
          }
        ],
        "flex": 0
      },
      "styles": {
        "footer": {
          "separator": True
        }
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://i.imgur.com/cTUCYBi.png",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "backgroundColor": "#FFFFFF"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "咖啡豆的產區",
            "weight": "bold",
            "size": "xl",
            "margin": "md"
          },
          {
            "type": "text",
            "text": "咖啡幾乎都以產區命名，主要種植在南北迴歸線間的亞熱帶和熱帶區，這個咖啡栽培區被稱為「咖啡帶」，不同產區的咖啡富有個別風味特色，主要分別為拉丁美洲區、非洲與亞洲太平洋地區等三大咖啡種植區域，從認識咖啡產地開始，尋找最適合自己的咖啡風味。",
            "margin": "md",
            "align": "start"
          }
        ],
        "action": {
          "type": "message",
          "label": "action",
          "text": "咖啡豆的產區"
        }
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "非洲區",
              "text": "非洲區"
            },
            "height": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "拉丁美洲區",
              "text": "拉丁美洲區"
            },
            "height": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "亞洲太平洋地區",
              "text": "亞洲太平洋地區"
            },
            "height": "sm"
          }
        ],
        "flex": 0
      },
      "styles": {
        "footer": {
          "separator": True
        }
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://i.imgur.com/oiZTwrl.png",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "backgroundColor": "#FFFFFF"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "咖啡豆處理法",
            "weight": "bold",
            "size": "xl",
            "margin": "md"
          },
          {
            "type": "text",
            "text": "咖啡果實需去除外皮、果肉和果膠等程序，並完成乾燥後方能烘焙，不同的處理方式，是影響咖啡豆風味的主因，在市面上常看到處理法有日曬、水洗、半水洗、蜜處理和低溫厭氧發酵作法等。",
            "margin": "md",
            "align": "start"
          }
        ],
        "action": {
          "type": "message",
          "label": "action",
          "text": "咖啡豆處理法"
        }
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "日曬處理法",
              "text": "日曬處理法"
            },
            "height": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "水洗處理法",
              "text": "水洗處理法"
            },
            "height": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "半水洗(濕刨法)",
              "text": "半水洗(濕刨法)"
            },
            "height": "sm"
          }
        ],
        "flex": 0
      },
      "styles": {
        "footer": {
          "separator": True
        }
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://i.imgur.com/G5oM5PV.png",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "backgroundColor": "#FFFFFF"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "咖啡豆處理法",
            "weight": "bold",
            "size": "xl",
            "margin": "md"
          },
          {
            "type": "text",
            "text": "咖啡果實需去除外皮、果肉和果膠等程序，並完成乾燥後方能烘焙，不同的處理方式，是影響咖啡豆風味的主因，在市面上常看到處理法有日曬、水洗、半水洗、蜜處理和低溫厭氧發酵作法等。",
            "margin": "md",
            "align": "start"
          }
        ],
        "action": {
          "type": "message",
          "label": "action",
          "text": "咖啡豆處理法"
        }
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "蜜處理",
              "text": "蜜處理"
            },
            "height": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "低溫厭氧發酵",
              "text": "低溫厭氧發酵"
            },
            "height": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": " ",
              "text": "低溫厭氧發酵"
            },
            "height": "sm"
          }
        ],
        "flex": 0
      },
      "styles": {
        "footer": {
          "separator": True
        }
      }
    }
  ]
}

def get_latin():
  return {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "weight": "bold",
            "size": "xl",
            "margin": "md",
            "text": "拉丁美洲區"
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "巴西",
              "text": "巴西"
            },
            "height": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "哥倫比亞",
              "text": "哥倫比亞"
            },
            "height": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "哥斯大黎加",
              "text": "哥斯大黎加"
            },
            "height": "sm"
          }
        ],
        "flex": 0
      },
      "styles": {
        "footer": {
          "separator": True
        }
      }
    },
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "weight": "bold",
            "size": "xl",
            "margin": "md",
            "text": "拉丁美洲區"
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "薩爾瓦多",
              "text": "薩爾瓦多"
            },
            "height": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "瓜地馬拉",
              "text": "瓜地馬拉"
            },
            "height": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": " ",
              "text": "瓜地馬拉"
            },
            "height": "sm"
          }
        ],
        "flex": 0
      },
      "styles": {
        "footer": {
          "separator": True
        }
      }
    }
  ]
}

def get_africa():
  return {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "weight": "bold",
        "size": "xl",
        "margin": "md",
        "text": "非洲區"
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
      {
        "type": "button",
        "action": {
          "type": "message",
          "label": "衣索比亞",
          "text": "衣索比亞"
        },
        "height": "sm"
      },
      {
        "type": "button",
        "action": {
          "type": "message",
          "label": "肯亞",
          "text": "肯亞"
        },
        "height": "sm"
      }
    ],
    "flex": 0
  },
  "styles": {
    "footer": {
      "separator": True
    }
  }
}

def get_asia():
  return {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "weight": "bold",
        "size": "xl",
        "margin": "md",
        "text": "亞洲太平洋地區"
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
      {
        "type": "button",
        "action": {
          "type": "message",
          "label": "印尼",
          "text": "印尼"
        },
        "height": "sm"
      },
      {
        "type": "button",
        "action": {
          "type": "message",
          "label": "越南",
          "text": "越南"
        },
        "height": "sm"
      },
      {
        "type": "button",
        "action": {
          "type": "message",
          "label": "巴布亞紐幾內亞",
          "text": "巴布亞紐幾內亞"
        },
        "height": "sm"
      }
    ],
    "flex": 0
  },
  "styles": {
    "footer": {
      "separator": True
    }
  }
}

def get_coffee_equipment():
  return {
  "type": "carousel",
  "contents": [
    {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "沖煮器材",
        "weight": "bold",
        "size": "xl"
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "message",
          "label": "摩卡壺",
          "text": "摩卡壺"
        }
      },
      {
        "type": "button",
        "height": "sm",
        "action": {
          "type": "message",
          "label": "義式濃縮咖啡機",
          "text": "義式濃縮咖啡機"
        },
        "style": "link"
      },
      {
        "type": "button",
        "action": {
          "type": "message",
          "label": "虹吸壺又稱賽風壺",
          "text": "虹吸壺又稱賽風壺"
        }
      }
    ],
    "flex": 0
  },
  "styles": {
    "footer": {
      "separator": True
    }
  }
},
    {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "沖煮器材",
        "weight": "bold",
        "size": "xl"
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "message",
          "label": "手沖咖啡",
          "text": "手沖咖啡"
        }
      },
      {
        "type": "button",
        "height": "sm",
        "action": {
          "type": "message",
          "label": "聰明濾杯",
          "text": "聰明濾杯"
        },
        "style": "link"
      },
      {
        "type": "button",
        "action": {
          "type": "message",
          "label": "法式濾壓壺",
          "text": "法式濾壓壺"
        }
      }
    ],
    "flex": 0
  },
  "styles": {
    "footer": {
      "separator": True
    }
  }
  }
  ]
}
  
def get_coffee_filter_cup():
  return {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "濾杯種類",
        "weight": "bold",
        "size": "xl"
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "message",
          "label": "錐形濾杯",
          "text": "錐形濾杯"
        }
      },
      {
        "type": "button",
        "height": "sm",
        "action": {
          "type": "message",
          "label": "扇型濾杯",
          "text": "扇型濾杯"
        },
        "style": "link"
      },
      {
        "type": "button",
        "action": {
          "type": "message",
          "label": "波浪/蛋糕型濾杯",
          "text": "波浪/蛋糕型濾杯"
        }
      }
    ],
    "flex": 0
  },
  "styles": {
    "footer": {
      "separator": True
    }
  }
}

def get_coffee_knife():
  return {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "刀盤種類",
        "weight": "bold",
        "size": "xl"
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "message",
          "label": "平刀",
          "text": "平刀"
        }
      },
      {
        "type": "button",
        "height": "sm",
        "action": {
          "type": "message",
          "label": "錐刀",
          "text": "錐刀"
        }
      },
      {
        "type": "button",
        "action": {
          "type": "message",
          "label": "鬼齒刀",
          "text": "鬼齒刀"
        }
      }
    ],
    "flex": 0
  },
  "styles": {
    "footer": {
      "separator": True
    }
  }
}

def get_coffee_filter():
  return {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "濾網",
        "weight": "bold",
        "size": "xl"
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "message",
          "label": "濾紙",
          "text": "濾紙"
        }
      },
      {
        "type": "button",
        "height": "sm",
        "action": {
          "type": "message",
          "label": "金屬濾網",
          "text": "金屬濾網"
        }
      },
      {
        "type": "button",
        "action": {
          "type": "message",
          "label": "法蘭絨濾布",
          "text": "法蘭絨濾布"
        }
      }
    ],
    "flex": 0
  },
  "styles": {
    "footer": {
      "separator": True
    }
  }
}
