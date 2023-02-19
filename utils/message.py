def get_new_event():
  return {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png", #圖片
        "size": "full",
        "aspectRatio": "4:3",
        "aspectMode": "cover"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "Brown Cafe",
            "weight": "bold",
            "size": "xl"
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "商品詳情",
              "text": "Brown Cafe 商品詳情"
            }
          },
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "立即購買",
              "uri": "https://famistore.famiport.com.tw/317733/index.php?action=fmall_12267038"
            }
          }
        ]
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
        "size": "full",
        "aspectRatio": "4:3",
        "aspectMode": "cover"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "Brown Cafe",
            "weight": "bold",
            "size": "xl"
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "商品詳情",
              "text": "Brown Cafe 商品詳情"
            }
          },
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "立即購買",
              "uri": "https://famistore.famiport.com.tw/317733/index.php?action=fmall_12267038"
            }
          }
        ]
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
        "size": "full",
        "aspectRatio": "4:3",
        "aspectMode": "cover"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "Brown Cafe",
            "weight": "bold",
            "size": "xl"
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "商品詳情",
              "text": "Brown Cafe 商品詳情"
            }
          },
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "立即購買",
              "uri": "https://famistore.famiport.com.tw/317733/index.php?action=fmall_12267038"
            }
          }
        ]
      }
    }
  ]
}

def get_coffee_roasting():
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
            "text": "淺談咖啡烘焙",
            "weight": "bold",
            "size": "xl",
            "margin": "md"
          },
          {
            "type": "text",
            "text": "關於咖啡烘焙的二三事",
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
              "label": "什麼是咖啡烘焙",
              "text": "什麼是咖啡烘焙"
            },
            "height": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "咖啡風味的關鍵",
              "text": "咖啡風味的關鍵"
            },
            "height": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "如何挑選咖啡烘焙機",
              "text": "如何挑選咖啡烘焙機"
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







