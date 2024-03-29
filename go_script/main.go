package main

import (
	"fmt"
	"net"

	tgbotapi "github.com/go-telegram-bot-api/telegram-bot-api/v5"
)

var bot, err = tgbotapi.NewBotAPI("5288667624:AAFBARM244Me22WXxZiTbK1r8kTfqAgM01I")

func main() {
	go checkErrors(err)
	go checkErrors(db_err)
	go socketHandler()
	defer db.Close()

	bot.Debug = true

	u := tgbotapi.NewUpdate(0)
	u.Timeout = 60

	updates := bot.GetUpdatesChan(u)

	for update := range updates {
		if update.CallbackQuery != nil {
			go CallbackQueryHandler(update)
		} else if update.Message != nil {
			go UserHandler(update)
		}
	}
}

func socketHandler() {
	listener, _ := net.Listen("tcp", "192.168.88.95:8001")
	for {
		connection, err := listener.Accept()
		if err == nil {
			go handleSocketConnection(connection)
		}
	}
}

func checkErrors(err error) {
	if err != nil {
		fmt.Println(err)
	}
}
